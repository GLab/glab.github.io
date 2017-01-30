---
layout: manual
title: User Manual
manual: user
manpage: connection/packet_capturing
category: manuals
---

# Packet Capturing

ToMaTo can capture all packets travelling over any connection to a pcap file. This is done from the outside, meaning that your element's will not be affected by this.


## Set-Up

To set up packet capturing, open the target connection's config window and select the _Packet Capturing_ tab. Here, you can enable packet capturing, and select whether you wish to create a downloadable file, or view them live via network.

The captured packets are saved to a rotating set of files holding at most 50 MB of data.

You can also define a filter for packets, meaning that only respective packets are included in the resulting dump. The filter syntax are [PCAP filter expressions](http://www.tcpdump.org/manpages/pcap-filter.7.html).

## Access to Download

When you set packet capturing to be downloadable, the connection's right-click menu contains a _Download Capture_ entry which will automatically start a download of the respective file.


## Access to Live-Viewing

When you set packet capturing for live viewing, the connection's right-click menu contains a _Live capture info_ entry which will open a window with information about the TCP stream as well as a prepared wireshark command you can use in your terminal.


## Timestamps

The timestamp in the capture files do not exactly correspond with the time of sending the packet in the virtual machine since the scheduling might introduce a delay. However the timestamp is guaranteed to be between the time of sending and the time of the forwarding to the connection.

Also note that [hosts](../../site_host) (which are distributed over multiple continents) may have a clock offset to each other, which is usually below 1s.


## Analysis programs

ToMaTo generates capture files in the [pcap format](http://en.wikipedia.org/wiki/Pcap). When downloaded from the hosts multiple capture files are packed into a tar.gz archive.

The capture files created by ToMaTo can be used by a lot different programs:

* [Wireshark](http://www.wireshark.org) - a graphical pcap explorer an analysis tool
* [tcpreplay](http://tcpreplay.synfin.net/) - a Linux tool to replay pcap files

