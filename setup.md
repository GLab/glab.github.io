---
layout: default
title: Setup
category: join
---

# Setup ToMaTo

There are two possible setups of ToMaTo: federated mode and island mode.

<div class="row" markdown="1">

<div class="col-xs-12 col-md-6" markdown="1">

## Federated mode

In shared mode, all hosts are accessible by the whole ToMaTo community and in return all ToMaTo hosts can be accessed through the federation. 
This mode is the recommended mode for all new sites that want to contribute to the community.

### Installation instructions

1. All hosts need to be installed with a compatible operating system and the ToMaTo hostmanager needs to be installed on all hosts. Please refer to the [installation instructions](http://tomato.readthedocs.org/en/latest/hostmanager/tomato/installation/). If needed, [support](mailto:support@tomato-lab.org) will be provided.
2. Please add the [backend certificate](http://master.tomato-lab.org/key.pem) to the hostmanagers as described in the [documentation](http://tomato.readthedocs.org/en/latest/hostmanager/tomato/backends/).
3. Contact the [support](mailto:support@tomato-lab.org) to get your new hosts listed on the shared backend.

</div>
<div class="col-xs-12 col-md-6" markdown="1">

## Island mode

In island mode, a full ToMaTo installation including backend, web-frontend is run. This installation is completely separate from the ToMaTo community.
The ToMaTo backend and the web-frontend need to be installed on a dedicated host. This host can be a virtual machine, it can even be *hosted* on a node running the ToMaTo hostmanager. 

### Installation instructions

1. The ToMaTo backend and the web-frontend need to be installed on the dedicated host. The installation should be accessible via HTTP with a browser.
2. All hosts need to be installed with a compatible operating system and the ToMaTo hostmanager needs to be installed on all hosts. Please refer to the [installation instructions](http://tomato.readthedocs.org/en/latest/hostmanager/tomato/installation/).
3. The backend certificate (accessible via `http://MY_TOMATO_ISLAND/key.pem`) must be added to all hosts as described in the [documentation](http://tomato.readthedocs.org/en/latest/hostmanager/tomato/backends/).
4. Now the hostmanagers can be added to the backend and should be available as hosts.

</div>
</div>
