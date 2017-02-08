---
layout: manual
title: User Manual
manual: user
manpage: element/switch
category: manuals
---

# Switches

![](../../img/switches.png)

Switches are part of the VPN elements of ToMaTo. They allow to connect devices with each other in virtual private networks.
Hence connected elements are isolated from other elements or the internet as long as they are not connected to each other (or the internet).

Currently there are 3 types of switches available:

  * Hub: Incoming packets will be broadcasted to **all** connected devices. It uses _Tinc VPN_ to connect elements with each other.
  * Switch (Tinc): Forwards packets targeted to a specific port. It also uses _Tinc VPN_.
  * Switch (VpnCloud): Forwards packets targeted to a specific port. It uses [VpnCloud](https://github.com/dswd/vpncloud.rs), a UDP-based VPN solution.

