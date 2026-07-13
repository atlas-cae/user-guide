---
title: Know The Disk
description: Keep your data on Atlas intelligently
published: true
date: 2026-07-13T09:12:35.478Z
tags: filesystem, drives, disks, space, storage, files
editor: markdown
dateCreated: 2026-04-19T16:17:27.527Z
---

# About Atlas's File System
Atlas has a complicated file system which is to be used responsible. We can generalize three locations that are assigned to users:
1. Your `/home/student` directory. When your account is created, this directory comes with it. As previously mentioned, **users only login to the login/head nodes**. This means all users are sharing a collective of only 512GB data. Also, the home directories are not synced in between the two login nodes. When the shift occurs, any data there leaves you stranded.

> The `/home/student` is not for **heavy** or **permanent** data. Use it for scripts and logs. We advise moving results to your laptop soon after you have achieved your objective. 
{.is-warning}
2. The `/scratch/student` on the compute nodes. There is one just for you on each compute nodes (there are ten compute nodes). The disk is a promising 2TB. But don't keep data lying there. This is a scratch space to facilitate computation by reading from an SSD instead of over the network. Besides, your compute node might change the next time you submit a job - data lying on the SSD of an older node won't do you any good. Again, clear the scratch once you've completed a project.
3. The `/data/student` on the networked filesystem. This is where you keep your heavier, more permanent data. This disk is backed up to keep your data safe and sound. 

## Where to Keep What
Here are some helpful pointers from the sysadmins,
- When you start a project, copy your **python scripts** in the `/home/student` directory. Make a new folder there for each project to keep things organized. 
> **Advice:** Use git.
{.is-info}

- Copy your **datasets** over the network using *scp* or *sftp* to `/data/student` (more on that later). Once again, create appropriate directories - it keeps things neat.
- Since you can't login to compute nodes, you can't directly access `/scratch/student`. Use it through your batch scripts. Copy your datasets and scripts over to this space and copy back your results. Clear this space soon after - it makes you a responsible user.

## Summing Up
This page was meant to give users an insight of the cluster's available space. An understanding of this helps in better operation and also allows one to make the most out of this facility.

Next: [ImportingYourData](/UsingAtlas/ImportingYourData)
 