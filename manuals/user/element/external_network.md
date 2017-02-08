---
layout: manual
title: User Manual
manual: user
manpage: element/external_network
category: manuals
---

# External Network

External Networks allow access to external networks or testbeds.
External networks have to be defined and configured by hostmanagers or administrators.
If the external networks

{:.alert .alert-warning}
Network segments should not have multiple network exits. This could cause loops in the network and hence network crashes.

### Kind

The kind of an external network defines to what network type the tunnel connects to.
ToMaTo uses a hierarchical order for network kinds.

For example:
If a user chooses an external network of kind _Internet_, he allows ToMaTo to choose from any defined internet connection from any site.
Whereas a user choosing an external network of kind _Internet (TU KL)_, he restricts the tunnel to a network bridge on a host from TU KL.

### Same Network

This option forces external networks which use the above mentioned hierarchical order to use the same subkind.