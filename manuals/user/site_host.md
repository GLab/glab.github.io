---
layout: manual
title: User Manual
manual: user
manpage: site_host
category: manuals
---

# Sites and Hosts

Experiments in ToMaTo are run on _hosts_. Whenever you [prepare](../element/action#prepare) an [element](../element), the backend's load balancer will automatically select a suitable host for every element. Different elements will most likely be located on different hosts.

Hosts are organized by _sites_. Sites are usually locations like a certain datacenter, meaning that hosts on the same site usually have a high-quality connection to each other. Since [connections](../connection) between elements are always subject to the connection between their hosts, the selection of sites will have measureable effect on your experiment.

{:.alert .alert-info}
You can see statistics about the connections between the different sites of the ToMaTo testbed [here](https://master.tomato-lab.org/map/). When you click on a site, you can select any link to another site.

You cannot control on which host an element will be deployed. However, you can select the site for each individual element, or for the whole [topology](../topology).
