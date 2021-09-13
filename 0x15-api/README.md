# 0x15. API

-   By Sylvain Kalache, co-founder at Holberton School
-   Ongoing project - started 09-13-2021, must end by 09-14-2021 (in about 11 hours) - you're done with 0% of tasks.
-   Checker will be released at 09-13-2021 03:36 PM
-   QA review fully automated.

## Background Context

[![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/897638f42eb1bad6605d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210913%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210913T161405Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=49430b57ef12c96b18dd131937a828ee1a75e38c1ad46f7fd469f47a0b324438)](https://youtu.be/-2kyU6-j8ZQ)

Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.

One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.

This is a perfect example of a task that is not suited for Bash scripting, so let’s build Python scripts.

## Resources

**Read or watch**:

-   [Friends don’t let friends program in shell script](https://intranet.hbtn.io/rltoken/6isWaTEpGTrwhzCCG5s_Tw "Friends don't let friends program in shell script")
-   [What is an API](https://intranet.hbtn.io/rltoken/I-XLIq5AwH-j29xJtzr6bQ "What is an API")
-   [What is an API? In English, please](https://intranet.hbtn.io/rltoken/I1nC8rhySGahG3gXYBfDPA "What is an API? In English, please")
-   [What is a REST API](https://intranet.hbtn.io/rltoken/6_OAlRYOGUuegPfyd4FUVg "What is a REST API")
-   [What are microservices](https://intranet.hbtn.io/rltoken/lewYS0z2RuFuiIkIgaCHSA "What are microservices")
-   [PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry](https://intranet.hbtn.io/rltoken/lEisphllQEYAs5yg26Ng0w "PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry")

## Learning Objectives

-   What Bash scripting should not be used for
-   What is an API
-   What is a REST API
-   What are microservices
-   What is the CSV format
-   What is the JSON format
-   Pythonic Package and module name style
-   Pythonic Class name style
-   Pythonic Variable name style
-   Pythonic Function name style
-   Pythonic Constant name style
-   Significance of CapWords or CamelCase in Python
