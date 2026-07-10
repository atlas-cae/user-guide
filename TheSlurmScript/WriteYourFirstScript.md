---
title: Write Your First Script
description: Understand how the slurm scripts work
published: true
date: 2026-07-10T17:18:50.095Z
tags: 
editor: markdown
dateCreated: 2026-06-22T04:48:10.183Z
---

# Write Your First Script
Understanding how Slurm works with scripts is crucial, especially to able to use Atlas effectively. Below is a generic rundown of a simple sample script that was used to train a CNN model to distiguish between Cats and Dogs.

> The key to writing a successful script is writing the scripts as if you were on a session on the node in question itself. Whatever you would write in the terminal, in sequence, goes in the script.
{.is-success}


## The Headers
The script starts off with the batch headers that tell Slurm what resources to use.

```bash
#!/bin/bash
#SBATCH --job-name=test_model
#SBATCH --nodelist=argon01
#SBATCH --cpus-per-task=6
#SBATCH --mem=4G
#SBATCH --gres=gpu:1
#SBATCH --output=/home/testuser/animals/logs/job_%j.log
#SBATCH --error=/home/testuser/animals/logs/job_%j.err
```

Here is a summary of the header:
- The job name is the identifier that will help you single out your running instance on the cluster (when you run `squeue`, for example).
- The output directory, outputs whatever the terminal outputs during the entire sequence of the script. Logs are recorded with the job id.
- The error directory records whatever comes out with an error message. These are also recorded against some job id.

## Creating Relevant Directories
As explained before, it is often helpful that heavier items that are required for training (the datasets, for example) be on the compute node itself. Users should organize their work by creating relevant directories in the scratch space provided to them.

```bash
mkdir -p /home/testuser/animals/logs
mkdir -p /scratch/testuser/animals/data
```

- Here, we create the directory for logs in the `/home` folder. Since logs are light, this is no problem and is actually recommended since the `/home` dircetory is most accessible to the user.
- Secondly, we create a data directory under the `animals` folder where we shall be copying our relevant dataset.

## Copy Your Dataset
After creating the directories, you should copy your items. 

```bash
cp -r /data/testuser/PetImages/ /scratch/testuser/animals/data
```

Make sure that you have your dataset on the headnode first. Do that in the `/data` directory, not the `/home` directory. Then copy from there.

## Load Your Modules
Atlas uses modules to organize Python libraries for AI/ML workloads. We have,
1. Python3.10: One module for Pytorch, Another for TensorFlow
2. Python3.12: One module for Pytorch, Another for TensorFlow
3. Python3.14

To use TensorFlow,

```bash
module load python/3.10 #change the version to 3.12 if needed
module load 3.10/tf_base # change the version to 3.12 if needed
```

To use PyTorch,

```bash
module load 3.10/pt_base #change the version to 3.12 if needed
```

But before loading these, make sure to source modules,

```bash
source /etc/profile.d/lmod.sh 
module use /opt/atlas/modulefiles/ 
```

Also,
```bash
module purge
```
This helps clear all variables and paths and cleans up the space for you.

Once you have loaded the modules, you can make environments within them for additional libary installations.

### Optional: Stack Your Own Environment
Missing libraries that we did not provide pre-built? Don't worry, you can stack on top of the existing modules. This way you use the existing environments for Pytorch/Tensorflow and include all the additionaly libraries for your use case in your custom environment.

```bash
python -m venv --system-site-packages my_stacked_env
source my_stacked_env/bin/activate

pip install libraryname
```

You only need to include this once in your script, run it and it is installed. To just activate your custom environment (after you are done with installations), include,

```bash
source my_stacked_env/bin/activate
```

## Run Your Script
Finally, run your script,

```bash
python3 /home/testuser/animals/train.py
```

## Summing Up
This explained how a basic Slurm script would work for a simple AI workload. Remember, the key to writing the script is to write it as if you were in a terminal session itself. 

> Using absolute path everywhere helps.
{.is-info}
