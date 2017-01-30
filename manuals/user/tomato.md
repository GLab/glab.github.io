---
layout: manual
title: User Manual
manual: user
manpage: tomato
category: manuals
---

# ToMaTo

The Topology Management Tool (ToMaTo) is a topology-centric network testbed, giving researchers the possibility to run their software in specifically designed virtual networking topologies.

ToMaTo is a federated testbed, controlled by a central backend, and accessible via an [API](../api) or a web frontend.

## Basic experiment procedure

{:.alert .alert-info}
Experiments in ToMaTo are organized in topologies.

When conducting an experiment, a user will design and create a [topology](../topology), i.e., a set of virtual devices, so-called [elements](../element), with [connections](../connection) between each other. The user can then [prepare](../element/action#prepare) them, meaning that they will be deployed on automatically selected [hosts](../site_host#host). After this step, the user can [start](../element/action#start) them. When everything is started, the user has full console access to the elements, added with special ToMaTo operations for the transmission of files and commands. This can be used to conduct experiments - manually or automatized. After the experiment, the respective topology should be [destroyed](../element/action#destroy) to avoid unnecessary server load.

## Federations

The ToMaTo testbed consists of multiple organizations, i.e., a university company, or similar entity. Every user and every host belongs to an organization. The distinction of organization allows a more fine-grained setting of permissions.
The organizations taking part in the ToMaTo testbeds form the _ToMaTo consortium_.

{:.alert .alert-info}
You can see the member of the ToMaTo consortium [here](https://master.tomato-lab.org/organization/).

## User Accounts

User accounts, [including yours](../account), are the key to access ToMaTo. Every user account has certain permissions on what they can do in ToMaTo. Access to topologies is also subject to authorization, meaning that different users may have access to different kinds of operations on different topologies. Depending on the permissions, a user account can, in addition to running experiments, manage users or hosts of its own organization, manage resources like [templates](../element/template), or monitor the status of the whole testbed infrastructure. If you have access to these advanced permissions, you should conduct the [respective manual](/manuals) for these.

