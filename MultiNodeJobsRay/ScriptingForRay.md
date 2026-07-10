---
title: Scripting For Ray
description: Learn how to use Ray with Slurm
published: true
date: 2026-07-10T17:02:14.426Z
tags: slurm, batch script, jobs, ray, multi-node, distributed processing
editor: markdown
dateCreated: 2026-07-10T14:14:42.430Z
---

# Scripts For Ray
As mentioned before, Atlas is not your standard Ray Cluster. The head and worker nodes aren't preconfigured and the daemons are not already running. Because Slurm is our primary workload manager, Ray is deployed *through* Slurm.

This presents a challenge in many aspects. For example, Ray initializes a standard port for communication. If multiple users start a Ray cluster, this'll create many conflicts. As a result, a highly custom script is modelled for usage of the Ray Cluster through Slurm.

Users are advised to follow the patterns of this script and report problems, if any, to the SysAdmin.

## Part One: The Header
All Slurm scripts begin with the header. Define your job name, resources and paths to log files.

```bash
#!/bin/bash
#SBATCH --job-name=ray-ddp-animals
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=2
#SBATCH --gres=gpu:1
#SBATCH --output=ray_%j.log
```
You may have one log file, or two separate ones for errors and logs respectively.

## Part Two: Initializing the Environment
Atlas provides modules for ease of environment managements. We provide pre-built PyTorch and TensorFlow environments and give users the option to stack on top of it. After the header, you load these environments,

```bash
source /etc/profile.d/lmod.sh 
module use /opt/atlas/modulefiles/ 

module purge
module load 3.10/pt_base
```

To use tensorflow, write the following instead of `module load 3.10/pt_base`.

```bash
module load python/3.10
module load 3.10/tf_base
```

To check what modules are available, run (through a batch script):

```bash
module avail
```

## Part Three: Building the Cluster
Next, we spin up the Ray Cluster. When you demand a certain number of nodes, Slurm assigns them as per their availability. The first of these nodes should be made Head of the Ray Cluster. The others should be assigned worker roles. This dynamic allocation is to be defined in part three of the script.

```bash
nodes=$(scontrol show hostnames "$SLURM_JOB_NODELIST")
nodes_array=($nodes)

head_node=${nodes_array[0]}
head_node_ip=$(srun --nodes=1 --ntasks=1 -w "$head_node" ip route get 1 | awk '{print $(NF-2); exit}')

echo "Allocated Cluster Nodes: ${nodes_array[0]} and ${nodes_array[1]}"
echo "Head Compute Node Identified: $head_node at Routeable IP: $head_node_ip"
```

This part of the script identifies the Head's IP. The rest of them become workers.

## Part Four: Dynamic Port Allocation
Ray's architecture involves GCS (Global Control Servive) which manages the meta-data of the Ray cluster. It stores all of the data in its memory and is crucial for the operation of the cluster. GCS requires a port for communication between the head and workers. Normally, this port is 6379. But we cannot have users simultaneously start Ray clusters at the same port - it would create conflicts. 

To solve this problem, we dynamically allocate port numbers that are related to the job IDs of the Slurm job. Dynamic ports are also allocated to the Ray dashboard.

```bash
BASE_PORT=20000
D_PORT=30000
DYNAMIC_PORT=$((BASE_PORT + (SLURM_JOB_ID % 5000)))
DASHBOARD_PORT=$((D_PORT + (SLURM_JOB_ID % 5000)))
```

## Part Five: Defining GCS Orchestration Address
Next, we must let GCS know where the head is. It will initialize on the dynamic port on the IP address of the Ray Head.

```bash
ip_head="$head_node_ip:$DYNAMIC_PORT"
export ip_head
export RAY_ADDRESS="$ip_head" 
```

## Part Six: Creating a Temporary Storage
To store session data, we create a temporary storage directory that we'll delete at the end of the script. This is to make sure we are on track and no data is lost mid-session.

```bash
export RAY_TMPDIR="/tmp/ray/user_${USER}_job_${SLURM_JOB_ID}"
mkdir -p "$RAY_TMPDIR"
```

## Part Seven: Identifying the Network
We must also tell Ray what network are we using. We do this by defining network sockets, etc.

```bash
export NCCL_SOCKET_IFNAME=enp4s0
export NCCL_DEBUG=INFO
```

## Part Eight: Start the Ray Head
Now that everything is properly set for the Ray cluster, we initialize the Ray head.

```bash
echo "Starting Ray Head Daemon on $head_node..."
srun --nodes=1 --ntasks=1 -w "$head_node" \
    ray start --head --node-ip-address="$head_node_ip" --port=$DYNAMIC_PORT \
    --dashboard-port=$DASHBOARD_PORT --disable-usage-stats \
    --num-gpus=1 --num-cpus=2 --block &

sleep 15 #give some time to stabilize
```

## Part Nine: Start the Ray Workers
Next, start the workers on all the other nodes except for where the head is initialized.

```bash
for worker_node in "${nodes_array[@]:1}"; do
    echo "Starting Ray Worker Daemon on $worker_node..."
    # Explicitly pass resource boundaries matching current script profile 
    srun --nodes=1 --ntasks=1 -w "$worker_node" \
        ray start --address="$ip_head" --num-gpus=1 --num-cpus=2 --block &
done

sleep 15 #give some time to stabilize
```

## Part Ten: Start Your Script
Finally, start your training/workload.

```bash
python3 test.py
```

## Summing Up
This was the sample script for running a Ray cluster and scaling your workload on a Slurm cluster using it. This script has been tested for some workloads and works well. However, there might be some unidentified edge cases where it fails. We appreciate users reaching out if they face a problem.
