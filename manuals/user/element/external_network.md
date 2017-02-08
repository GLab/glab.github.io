---
layout: manual
title: User Manual
manual: user
manpage: element/external_network
category: manuals
---

# External Network Connectors

External Network Connectors allow access to external networks or testbeds.
A list of available external networks to choose from is available at _External Network_ under the _Resources_ entry in the main menu. ([→ go now](https://master.tomato-lab.org/external_network/))

If the external network is located on a different site than the rest of the connected elements, 
packets have to be forwarded to this site and hence have a higher delay.

{:.alert .alert-warning}
Network segments should not have multiple network exits. This could cause loops in the network and result in network crashes.

## Configuration

An external network connector element has the following configuration options

### Kind

The kind of an external network defines to what network type the tunnel connects to.
ToMaTo uses a hierarchical order for network kinds.

For example:
If a user chooses an external network of kind _Internet_, he allows ToMaTo to choose from any defined internet connection from any site.
Whereas if a user chooses an external network of kind _Internet (TU KL)_, he restricts the connection to a host from TU KL.

### Same Network

This option forces external networks which use the above mentioned hierarchical order to use the same subkind.
