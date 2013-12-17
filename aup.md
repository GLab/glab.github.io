---
layout: default
title: Acceptable Use Policy
category: join
---

# Acceptable Use Policy
By using the testbed you accept the following rules and conditions.
Violations against these rules can be reported to <abuse@tomato-lab.org>.


## General rules
The following activities/experiments are prohibited on the testbed:

* **Anything that is unlawful**. Be aware that you must abide by...
  - your local laws,
  - the laws of the country of the platform provider (Germany),
  - the laws of all of the countries of the resource providers.
* **Commercial activities** that have not been accepted by the platform provider. This especially includes selling the resources that are provided in any way.
* **Hacking/Denial of Service attempts** on external services, platform infrastructure or other experiments.

**Do not share your account credentials**, use topology permissions for shared experiments.

### Communication is key
When experiments show strange behavior, administrators have to decide whether this is expected behavior or an experiment that ran out of control.
Without enough information about your experiment, administrators might come to the wrong conclusion and terminate it.
You can prevent this from happening if you...

* ask before you do something that might not be allowed.
* provide a good description of your experiment.
* keep your supervisor informed about your experiment.
* inform administrators in advance of strage behavior.
* are reachable during critical phases of your experiment.


### Be fair to others

* Try to **minimize your resource footprint** as much as you can.
* Try your experiment at small scale first and increase the size when it worked.
* **Shut down your experiment** when you are not working on it.
* **Try not to interfere** with other experiments or normal network operation.


## Internet rules
On public external networks (i.e. the Internet) additional rules apply.

### Address dicipline

* Obtain **IP addresses via DHCP** and only use these addresses.
* Do not try to spoof addresses.
* **Do not run a DHCP server** or interfere in any way with DHCP functionality
* Only use addresses as long as you need them and limit your topology to one public IPv4 address

### Security

* **Secure all services** that you run on publically reachable nodes.
* Do not run SSH with the default password.

Please note that under certain jurisdictions (e.g. Germany, "Störerhaftung") you can be hold liable for damage that is done by others using resources that you are responsible for.
By using a public address, you agree to free the platform provider and the resource providers from this kind of liabilty by taking over both the control as well as the responsibility over the resources of your topology.

### Prohibited services
The following services are in general prohibited and must not be provided to an external network.

* DHCP servers (clients are ok)
* Telnet
* FTP
* Filesharing networks (e.g. Bittorrent)

### Access restrictions
Do not access any content via public external networks that you do not normally have access to with your own pc.
This especially applies to websites hosting research papers and campus internal services.


## Consequences
Depending on the severity and urgency of the case the following actions may be taken immediatly even without prior warning.

* Termination of the topology or parts of it with the risk of data loss and damages to running experiments
* Account termination
* Notice to site supervisors/authorities
* Legal consequences


## Exceptions to rules
In certain cases, exceptions to these rules are possible when they are crucial to an experiment.
Please contact administrators before planning an experiment if you need an exception to one of these rules.


## Privacy
By using the platform you allow the platform provider to collect and keep the following data:

* The resource usage of your topology and all its components is collected and stored as long as your topology exists. The platform provider may store this data longer if it is neccesary for platform operations.
* Your actions on your topology and all components is logged and stored for two years for debugging reasons.
* All data that you enter into your topology (also disk images) are stored as long as needed to execute the requested operations.

Please note that administrators can access all of your data for debugging or troubleshooting reasons.


## Warranty

* This testbed is provided on the basis of best effort, thus no guarantees are given on resource availability.
* The software is provided as is, there are no guarantees on availability, usability or support.
* Data stored in the topology might be lost due to node failures, please create backups of all valuable data.
* The providers of the testbed and the testbed resources are not liable in case of data loss or damages of any kind.
