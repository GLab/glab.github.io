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

[TODO]

### Generating Certs

For internal communication, the ToMaTo modules require certificates that are signed by the same CA. You can use the tomato-ctl tool to generate a CA if missing, and all certificates, by running `./tomato-ctl.py gencerts` - these will be created automatically in the config directory. The CA's private/public key pair is stored in the docker directory.

When distributing ToMaTo over multiple hosts, run `gencerts` on one host, then transmit the public/private key pair to the other hosts' docker directories, and run `gencerts` on these hosts, too.

### Starting and Stopping

Once you have set up `tomato-ctl.conf`, you can simply start all containers by running `./tomato-ctl.py start`. To stop ToMaTo, run `./tomato-ctl.py stop`. To control individual services, you can use `./tomato-ctl.py backend_core start`, for example. To see more options, run `./tomato-ctl.py help`.

