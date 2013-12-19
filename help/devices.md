---
layout: default
title: Devices
category: help
---
# Devices

## Introduction

## States

### Created
A device which is created does not exist as a virtual machine yet.
"created" means the device is defined in a topology. It also doesn't have a disk image.

### Prepared
A prepared device does exist as a virtual machine with its own disk image.

When becoming prepared, the disk image will be created from the set [template](../device_template).
This disk image will be deleted when the device gets destroyed.

A prepared device is not running.

### Started
A started device is a running virtual machine.



## Editor
Devices are represented by computer icons.

You can determine the state of a device by its attached icon. A created device does not have an icon attached to it; a prepared device has a ![prepared](../img/prepared.png) and a started device has a ![started](../img/started.png) on it.
