---
layout: default
title: Connection Configuration Window
category: help
---
# Connection Configuration Window

## Introduction

Here you can set link emulation and packet capturing for network connections.


## Link Emulation

### Guarantees

Connections between different sites use the Internet and are therefore subject to the Internet's best-effort guarantee.
Thus, additional delay may apply and it may happen that you don't get the full bandwidth.

### Directions

You can set different directions for each direction.

The easiest way to determine a direction is to look at the arrow in the direction field.


**Bandwidth:** Bandwidth in kbit/s in one direction. Note that the two directions are seperate channels.

**Delay:** Delay in ms for the packet.

**Jitter:** Random jitter range for the delay in ms. The jitter will be added to or subtracted from the delay.

**Distribution:** Distribution for the jitter.

**Loss Ratio:** Loss ratio in % to be applied to packets.

**Duplication Ratio:** Duplication ratio in % to be applied to packets.

**Corruption Ratio:** Corruption ratio in % to be applied to packets.


## Packet Capturing
Captured packets can either be downloaded or viewed live.
Downloadable Packets can be sent directly to Cloudshark for viewing (With a limit of 10MB).

You can get the captures from the connection's right-click menu.

**Capture Mode:**

 * For download: Download for Wireshark or Cloudshark.
 * Via network: Live Viewing

**Packet filter expression:** Filter packets by a wireshark filter. More information at the [wireshark-filter](http://www.wireshark.org/docs/man-pages/wireshark-filter.html) man page.
