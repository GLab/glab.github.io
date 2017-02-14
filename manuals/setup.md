---
layout: manual
title: Testbed Manager Manual
manual: setup
manpage: home
category: manuals
---

# Home

This is the ToMaTo testbed manager manual. It is aimed at people who want to set up and manage their own testbed using the ToMaTo software.

You should have understood the core concepts from the [users' manual](../user). This manual will link to the other manuals where necessary, so there is no deep knowledge about other topics required.

## Overview over this manual.

Before continuing, please read the [introduction](introduction). Here, you will learn the basics about the ToMaTo architecture.

To set up your ToMaTo instance, you must know about these topics:

* [Introduction](introduction): Basic information about ToMaTo's architecture
* [Installation](installation): How to install the ToMaTo software on your server
* [Config](config): Set up your config files
* [Container Management](tomato-ctl): Manage the Docker containers
* [Admin User](admin): First login and security
* [Resources](resource): Manage templates, profiles, external networks, and web resources

Additionally, the following sections may help you managing your testbed

* [Dump Manager](dumpmanager): ToMaTo's internal error management
* [Troubleshooting](troubleshooter): Most common problems and their solutions

## First-Time Set-Up
To set up your ToMaTo instance, please follow these steps:

* Install the software
* Configure tomato-ctl and config.yaml
* Set up certificates
* Start ToMaTo
* Log in with the default admin account and create your own user
* Log in with your user and remove the default admin
* Configure hosts (at least one)
* Configure templates
* Configure external networks
