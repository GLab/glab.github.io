---
layout: default
title: Node Requirements
category: join
---

# Node Requirements

Each ToMaTo node must meet some minimum requirements to be usable for the platform.

## Node Hardware

* Multiple cores with **at least 2 GHz**
* Support for **hardware virtualization** in the CPU
  - This means that the node must be physical and not a VM
  - You can check this requirement by executing:
    ``grep -qE 'flags.*(vmx|svm)' /proc/cpuinfo && echo "supported" || echo "not supported"``
* At least **12 GB RAM**
* At least **300 GB hard disk**

## Node connectivity

* At least 1 **GBit LAN** (site internally)
* Unfiltered access to the Internet
* At least one dedicated **public IPv4 address**

## Site requirements

* At least 1 MBit WAN (Internet access)

## Availability

* Planned availability of **at least 95% uptime**
* Technical support with reaction time within 3 work days