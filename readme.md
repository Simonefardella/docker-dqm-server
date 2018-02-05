# Supported tags
-   latest

# About this image
This image can be used as a starting point to run django-queue-manager server application.
It uses [Django-Queue-Manager](github.com/Simonefardella/django-queue-manager/tree/master/django-queue-manager) in 
the latest version to expose the server interface of DQM (formerly: django-queue-manager) in order to keep separate
the queues from teh core app.
The container picks up the wsgi entry point based on the environment variable `DJANGO_APP` during the execution of 
the `dqm_server.py`.

Django is already installed within the latest version.

The image does export port `8000`, so, if you have multiple queues, do a port forwarding directly from docker.

It has a volume defined to consume resources at `/django_app` needed for the DQM queue server workers.

# How to use this image

## Basic Setup

Starting a new container with the ready-to-production environment it's really simple, in a nutshell:

    FROM simonefardella/django-dqm
    ENV DJANGO_APP=helloworld                # will start a DQM server bound to port 8000 that uses the helloworld.settings wsgi callable to process all the enqueued tasks

## DJANGO REQUIREMENTS

This image, becomes with a built-in battery system that manages the pip requirements installation, in fact
if you want to install some python packages, you have to deploy the requirements.txt file in the same folder of your 
workdir `django_app`, the `/start.sh` will look for requirements.txt file, and install all requirements.

In any case, during the building process, the dockerfile will install the content of the `/build_requirements.txt` 
file, that contains:

- `Django`
- `mysqlclient`
- `django-queue-manager`

These packages will be installed in any case, because they are needed for the container purpose,
and because they need some libs that are removed after the image building, in order to keep the image very lightweight.

## THE EXTRA.SH

During startup, the `/start.sh` will look into the workdir `django_app` if there is a file called `extra.sh`. If that file 
exist, the content of the file will be executed, useful for doing some extra installation or extra operations.


## Executing one off commands of DQM Server

Simply use the shell via docker commands:

    docker exec -it <container_name_or_id> /bin/sh
    
-OR-
    
    Use the Rancher web-ui to get the shell directly from web interface

And then, use the reference of the official readme of DQM package, following the `Shell interface` section:
[Django-Queue-Manager](https://github.com/Simonefardella/django-queue-manager/tree/master/django-queue-manager#Run-the-Tasks-Queue-Server) 

# User Feedback

## Issues
If you have any problems with or questions about this image, please contact me through a GitHub issue.

## Contributing
You are invited to contribute new features, fixes, or updates, large or small.
Please send me a pull request.
