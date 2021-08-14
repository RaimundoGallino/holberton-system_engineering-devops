# 0x0B. SSH

## Background Context


Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away. Like level 2 of the application process, you will connect using `ssh`. But contrary to level 2, you will not connect using a password but an RSA key. We’ve configured your server with the public key you created in the first task of [a previous project](https://intranet.hbtn.io/rltoken/LZ_8pMANOAmpn5-tiwqiJQ "a previous project") shared in your [intranet profile](https://intranet.hbtn.io/rltoken/l4Ao4ESbI_hMB6s4mjBKRw "intranet profile").

You can access your server information in the [my servers](https://intranet.hbtn.io/rltoken/owYhGMuyPTY4OyvSGJljGQ "my servers") section of the intranet, each line with contains the IP and username you should use to connect via `ssh`.

**Note:** Your server is configured with an Ubuntu 16.04 LTS environment. You do **not** need to create a new virtual machine. If you decide you want to upgrade to Ubuntu 16.04, make sure to create a new VM. Do **not** attempt to upgrade your current Ubuntu 14.04 environment as that will inevitably be messy and can break things. Note that if you switch, none of your files and environment settings will be available and anything you need will have to be reinstalled or migrated.

## Resources


-   [What is a (physical) server - text](https://intranet.hbtn.io/rltoken/PXE-o9DWronMp4ETwADOpg "What is a (physical) server - text")
-   [What is a (physical) server - video](https://intranet.hbtn.io/rltoken/IfLc3lxSs4w5xdsFlRDPWw "What is a (physical) server - video")
-   [SSH essentials](https://intranet.hbtn.io/rltoken/qKJi0RXLqaCLkHLCLhiYNA "SSH essentials")
-   [SSH Config File](https://intranet.hbtn.io/rltoken/hnb0XaZQ0Nb_7QmSC6aV-w "SSH Config File")
-   [Public Key Authentication for SSH](https://intranet.hbtn.io/rltoken/zaO_H74BXLfsrQHzDW-QGQ "Public Key Authentication for SSH")
-   [How Secure Shell Works](https://intranet.hbtn.io/rltoken/SW2m2e0KMA2K1dXk_0M0CA "How Secure Shell Works")
-   [SSH Crash Course](https://intranet.hbtn.io/rltoken/8N-RlUma9lwGfyZp1_C-Wg "SSH Crash Course") (Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)


# Learning Objectives

-   Where servers usually live
-   What is SSH
-   How to create an SSH RSA key pair
-   How to connect to a remote host using an SSH RSA key pair
-   The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`