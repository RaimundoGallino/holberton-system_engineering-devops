# 0x0F. Load balancer

## Concepts

_For this project, students are expected to look at these concepts:_

-   [Load balancer](https://intranet.hbtn.io/concepts/46)
-   [Web stack debugging](https://intranet.hbtn.io/concepts/68)

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/275/qfdked8.png)

## Background Context

You have been given 2 additional servers:

-   gc-[STUDENT_ID]-web-02-XXXXXXXXXX
-   gc-[STUDENT_ID]-lb-01-XXXXXXXXXX

Let’s improve our web stack so that there is [redundancy](https://intranet.hbtn.io/rltoken/QiOC_I-8BeV4aNExIucC9Q "redundancy") for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

## Resources

**Read or watch**:

-   [Introduction to load-balancing and HAproxy](https://intranet.hbtn.io/rltoken/ngIXarEyu8jZwOL3Y30PLQ "Introduction to load-balancing and HAproxy")
-   [HTTP header](https://intranet.hbtn.io/rltoken/v32JmcDrSiOnFBfqzXvs_Q "HTTP header")
-   [Debian/Ubuntu HAProxy packages](https://intranet.hbtn.io/rltoken/BXGrW_6ocecWaOJb7OK_WA "Debian/Ubuntu HAProxy packages")

