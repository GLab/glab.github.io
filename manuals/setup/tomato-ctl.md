---
layout: manual
title: User Manual
manual: setup
manpage: tomato-ctl
category: manuals
---

# Container Management

As discussed in the [introduction](../introduction), backend and webfrontend are split into multiple modules, each running in its own [Docker](https://docker.com) container. This page will discuss the connections between the different containers, and will explain how the _tomato-ctl_ tool can be used to manage these containers.

## Prerequisites

The containers use special Docker images, which have been built during the [installation](../installation). These must be available on your system, as well as the ToMaTo software.

## Overview of Containers

As mentioned earlier, each module runs in its own container. Additionally, on every physical host that hosts at least one module, a MongoDB container is available, and all containers requiring the database are connected to this via Docker's networking features.

The containers automatically start their respective software, so starting the container is equivalent to starting the module.

On each host, you must specify the available modules via [tomato-ctl.conf](../config#tomato-ctl.conf).

## Using the tomato-ctl tool

The _tomato-ctl_ tool is the easiest way to create Docker containers from images and start them. You don't need to be familiar with Docker when managing ToMaTo with the tomato-ctl tool. The tool is located at `~/ToMaTo/docker/run/tomato-ctl.py`.

### Shared Directories

Depending on the module, containers have a number of shared directories with the host, meaning that they store their data on the host's file system (they are not shared between each other!). These directories usually include, among others, config, data, and logs.

By default, these directories are located in the docker directory, in a module-specific subdirectory.

Additionally, the code will be included from the respective directory in `~/ToMaTo`.

### Generating Certs

For internal communication, the ToMaTo modules require certificates that are signed by the same CA. You can use the tomato-ctl tool to generate a CA if missing, and all certificates, by running `./tomato-ctl.py gencerts` - these will be created automatically in the config directory. The CA's private/public key pair is stored in the docker directory.

When distributing ToMaTo over multiple hosts, run `gencerts` on one host, then transmit the public/private key pair to the other hosts' docker directories, and run `gencerts` on these hosts, too.

### Starting and Stopping

Once you have set up `tomato-ctl.conf`, you can simply start all containers by running `./tomato-ctl.py start`. To stop ToMaTo, run `./tomato-ctl.py stop`. To control individual services, you can use `./tomato-ctl.py backend_core start`, for example. To see more options, run `./tomato-ctl.py help`.

You can use the `restart` command to stop and start a container.

Due to Docker's internal linking, database container is a hard dependency for some modules to run. Thus, this container should be started first and stopped last. When using the `start` and `stop` commands for all modules, this is assured automatically.

The status of a containers (all or individually, as with start and stop) can be requested by running `./tomato-ctl.py status`. For the backend modules, tomato-ctl will automatically perform a check whether the software has started. However, because `backend_accounting` may be compiled on startup, this check may fail on the first start.

### Logs

You can view the logs of a container by running `./tomato-ctl.py backend_core logs` (or another module). use `logs-live` to view live logs.

### Shell

You can attatch to a shell on the container by running `./tomato-ctl.py backend_core shell` (or another module). This will result in a mongodb session for the database container, and a bash shell on the other containers.

### Backup

To create or restore a backup of the database, you can use `./tomato-ctl.py backup SOMENAME` and `./tomato-ctl.py restore SOMENAME`. The backup is stored 

