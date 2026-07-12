---
title: Get a User Account
description: To use Atlas, you must have a user account.
published: true
date: 2026-07-12T02:07:13.098Z
tags: user, accounts, registration, register
editor: markdown
dateCreated: 2026-04-19T15:09:11.426Z
---

# Register for Atlas
Atlas is not openly accessible to any user. The following conditions apply,
1. You must be on the **CAE network**.
2. You must have a **verified account** on the HPC.

Getting on the CAE network is easy. Connect to the institution's Wi-Fi/Wired Network on campus, in the libary or in your blocks. You'll be instantly able to access this page and login to the cluster. For the second condition, getting a verified account, read on.

## Getting a Verified Account
You can register for Atlas by filling out a [form](https://forms.cloud.microsoft/pages/responsepage.aspx?id=LqsRFStQLU69aPZ59Um1ooxwxWTgDtdFrLS9DAJATa5UN1BUVTMxS1lWNzlMVjJTQ1VIWktSSlFTRCQlQCN0PWcu&route=shorturl). You may also join our [Atlas Users' Teams](https://teams.microsoft.com/l/team/19%3Aemq1IfOzDisolFbwhyXpc6OJhyTDGVHR4waGCWz-k5o1%40thread.tacv2/conversations?groupId=9cfc21e3-1607-486c-8d88-4d5ad4b586ff&tenantId=1511ab2e-502b-4e2d-bd68-f679f549b5a2)

A verification email will give you your login credentials.

## Personalizing your Account
Once you get your credentials, get ready to login. On your terminal,
```bash
ssh student@192.168.24.100
```

Where **student** is your username. You will be prompted for a password. Enter the one provided on the verification email. Next, your personalization and security purposes, we advise you to change your password.
```bash
passwd
```

Enter the *previous password* and your *new password*. Now the account is truly yours.

## An Occasional Need To Troubleshoot
Sometimes, when you try to SSH your machine will throw this error at you
```bash
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
#yada yada
````

This is nothing to worry about. We allow users to login only to the login/head nodes and sometimes you are being managed by the *Back-up Head* instead of the *Primary Head*. 

Quickly run the following in your terminal. Make sure to replace *youruser* in the path with your username (the one on your laptop not HPC).
```bash
ssh-keygen -f "/home/youruser/.ssh/known_hosts" -R 192.168.24.100
```

SSH again - this time successfully,
```bash
ssh student@192.168.24.100
```

## Addons with the User Account
In addition to the user account, which gives you real estate on the head nodes much limited drive, Atlas's users get a directory on the HPC's more permanent file system. To access it, login using SSH then,
```bash
cd /data/student
```

There's your space! Add all your heavy datasets here. To learn more about managing space efficiently and responsibly, follow along.

## Summing Up
You now have a user account on Atlas's HPC. Let's move on to learning about the file systems and then onto submitting your first job for AI training.

Next: [Know Your Space](/UsingAtlas/KnowYourSpace)