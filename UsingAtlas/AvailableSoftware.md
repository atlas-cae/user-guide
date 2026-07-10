---
title: Available Software
description: Get to know what Atlas offers pre-built
published: true
date: 2026-07-10T17:36:46.227Z
tags: software, python, lmod, modules, pytorch, tensorflow
editor: markdown
dateCreated: 2026-07-10T17:14:34.645Z
---

# Available Software
Atlas offers pre-built environments for AI/ML workloads. We advise our users to check if their requirements are being fulfilled by these environments first before creating their own environments in their `/home` directory. 

## Versions of Python
Atlas offers three versions of Python

1. Python3.10 (Legacy Stable)
2. Python3.12 (Standard Stable)
3. Python3.14 (Bleeding Edge)

To activate any of these, include in your script

```bash
module load python/3.10 #3.12,3.14 etc
```

## AI/ML Environments
We offer environments for PyTorch and Tensorflow only for python versions 3.10 and 3.12.

### PyTorch
The libraries available for PyTorch are:

***torchvision torchaudio numpy pandas matplotlib scikit-learn scipy seaborn transformers datasets accelerate tqdm ipykernel wandb ray***

To load PyTorch,

```bash
module load 3.10/pt_base #or 3.12/pt_base
```

### TensorFlow
The librarues available for TensorFlow are:

***numpy pandas matplotlib scikit-learn scipy seaborn transformers datasets accelerate tqdm ipykernel wandb ray***

To load Tensorflow,

```bash
module load python/3.10 #or 3.12
module load 3.10/tf_base #or 3.12/tf_base
```

## An Important Note
Always clear your space of orphan variable names in the memory. 

```bash
module purge
```

Running the above before loading modules accomplishes it.

## Summing Up
It is important to know what an HPC offers pre-built as it removes the need to download requirements (latency). It is also more efficient to use the HPC this way because if every user were to create their own copies of libaries, it would waste a lot of disk space.

We advise users to take advantage of these provisions and demand more if needed. 

Next: 
