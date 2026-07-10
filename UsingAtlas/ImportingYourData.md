---
title: Importing Your Data
description: Copy your datasets and your python scripts
published: true
date: 2026-07-10T17:21:26.715Z
tags: datasets, scripts, copying, scp, sftp
editor: markdown
dateCreated: 2026-04-19T16:19:14.729Z
---

# Moving Files to Atlas
Since computation is to be performed on Atlas, it must have all your relevant files. Atlas is currently targeted for AI and ML so with that objective in mind, we'll train a simple Cat-vs-Dog CNN.

## Copying the Dataset
First we download the dataset from [Kaggle](https://www.kaggle.com/datasets/shaunthesheep/microsoft-catsvsdogs-dataset?resource=download). The structure of the downloaded and then unzipped folder is as follows,
```bash
sysadmin@sysadmin-HP-EliteBook-850-G4:~/Downloads/archive$ ls
'MSR-LA - 3467.docx'   PetImages  'readme[1].txt'
sysadmin@sysadmin-HP-EliteBook-850-G4:~/Downloads/archive$ tree -d
.
└── PetImages
    ├── Cat
    └── Dog

4 directories
```
The requirement of the python script we are using for training is such that we must only have the two folders `Cat` and `Dog`. The additional files are not required. We must be aware of this. To improve speeds of transfer, copy the `.zip` file.

```bash
scp archive.zip student@192.168.24.100:/data/student/
```

Once this is done, verify if your files are there. SSH into Atlas, then

```bash
ls /data/student
```
This should return `archive.zip`. Unzip it.
```bash
unzip archive.zip
```

Congratulations, your dataset has travelled safe.

## Creating/Copying Python Script
With the dataset copied, we must now create our project directory and copy in our python script. We can do this the raw way - via the terminal but VSCode makes things so much simpler and intuitive. 

1. Open VSCode and install the extension `Remote-SSH`.
2. Press `F1` to open the **Command Palette**. Type in **Remote-SSH: Connect to Host...**. Enter `student@192.168.24.100`, then press **Enter**. It shall prompt you for a password. Enter it.
3. Open the VSCode terminal. Make a new directory by entering,
```bash
mkdir animals
```
4. Go to the **File** menu and open the *animals* folder. You have your workspace now. 
5. Create a new file by the name *train.py*. Code.

## Summing Up
This does it for creating a copy of your files on Atlas. You are ready to train the model now.

Next: [Available Software](/UsingAtlas/AvailableSoftware)

