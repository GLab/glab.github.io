---
layout: manual
title: Testbed Manager Manual
manual: dev
manpage: rextfv
category: manuals
---

# Executable Archives

Executable archive is a technology providing the following features:

* [Upload](upload) data to a device
* [Execute](auto_exec) a certain script right after the upload, and monitor its execution
* Set a [custom status](custom_status) that is accessible via the ToMaTo API
* [Download](download) data from the device

Although these look like completely separate features, they all use the same technologies: [RexTFV and nlXTP](/about/publications/2014_A_networkless_data_exchange_and_control_mechanism_for_virtual_testbed_devices_TridentCom.pdf).

## Overview

Executable archives communicate with your device via the so-called _archive directory_. This is a special directory on your device which can be accessed from the host directly via the _network-less Execution and Transfer Protocol_ (nlXTP). This does not make use of traditional network interfaces, meaning that it will not influence your network experiments.

The archive directory is available at a certain location on your device, usually at `/mnt/nlXTP`. In some cases, the host cannot write into this directory, but reading is always possible. For more information about this, consult the respective device type descriptions in the [user manual](/manuals/user).

