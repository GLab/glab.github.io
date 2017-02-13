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

External network elements are located on a host, which acts as a gateway. If the external network is located on a different site than the rest of the connected elements, packets are forwarded to this site and hence have a higher delay.

{:.alert .alert-warning}
Network segments should not have multiple network exits. This could cause loops in the network and result in network crashes.

## Configuration

An external network connector element has the following configuration options

### Kind

The kind of an external network defines to what network type the tunnel connects to.
ToMaTo uses a hierarchical order for network kinds.

For example:
If you choose an external network of kind _Internet_, ToMaTo may use any host on any site to act as a gateway.
Whereas when selecting an external network of kind _Internet (TU KL)_, this would restrict the gateway selection to a host from the TU KL site.

### Same Network

This option forces external networks which use the above mentioned hierarchical order to use the same subkind.
