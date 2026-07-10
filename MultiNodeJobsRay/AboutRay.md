---
title: About Ray
description: Introducing Ray as means to scale your code efficiently.
published: true
date: 2026-07-10T14:13:13.793Z
tags: slurm, ray, scaling, multi-node, distributed processing
editor: markdown
dateCreated: 2026-07-10T14:13:13.793Z
---

# About Ray
Ray is an open-source framework that helps scaling AI and Python applications. By moulding your code according to the Ray standards, you essentially make your code valid for distributed and parallel processing without having to worry about the underlying dynamics. 

Other options for scaling include MPI (Message Passing Interface). Options like MPI have a steeper learning curve and for a researcher who is just interested in speeding up his simulations and training, it often becomes too much of an overhead. 

To learn more about Ray, visit [Ray's Official Documentation](https://docs.ray.io/en/latest/index.html).

## How do you Scale?
Putting a bunch of computers together and configuring them as a cluster does offer n-fold the computation prospects but it isn't always that easy to reap those benefits. Here is the fact, plain and bold:
> You **CANNOT** scale a standard code.
{.is-info}

You must always rewrite it in some way that'll help use the distributed resources. This can be very difficult to do (using protocols like MPI) or relatively easier (like what Ray has to offer).

## Ray AI Libraries
Ray offers 5 libraries to scale your AI/ML code. 
1. Data
2. Train
3. Tune
4. Serve
5. RLib

Each of them has its own purpose. To learn more, visit [Ray's Documentation](https://docs.ray.io/en/latest/index.html).

Currently, Atlas provides **Ray Data**, **Ray Train** and **Ray Tune**. Other provisions can be made subject to demand of users.

## Summing Up
By introducing Ray to Atlas, we provide means to our users to easily scale their code. Atlas is, however, not your standard Ray cluster - it uses Ray through Slurm. Users spin up their own Ray clusters against their jobs which dies when the job dies. This provision is custom to Atlas and require special scripting. Follow along to learn how to use Ray with Slurm.

Next: 