---
layout: manual
title: User Manual
manual: setup
manpage: introduction
category: manuals
---

# Introduction to ToMaTo's Architecture

This chapter will teach you the basics about ToMaTo's architecture and its implications on the set-up process.


## Overview

ToMaTo has a modular architecture. It consists of three different components:

* clients
* backend
* hostmanagers

[TODO: picture from the tomato paper]

### Clients

A client is any program that allows user interaction. The most important client is the webfrontend, which is usually hosted by the testbed administrator and allows access to ToMaTo via the user's web browser. Additionally, there is the CLI which allows users to call API functions directly. And at last, users may develop their own clients that connect to the API to run more complex functions.

There may be any number of clients running simultaneously.


### Backend

The Backend is the central component of ToMaTo and the representative of the whole testbed. It contains user management as well as host and resource management, is responsible for authorizational decisions, and store's all metadata about topologies, elements and connections. From the outside, the backend can be accessed via the ToMaTo API.

Although the backend looks like a single component to the outside, it is split into many services that communicate via an internal API.


### Hostmanagers

The hostmanager is a component that runs on a ToMaTo host, managing virtual machines and virtual connections on the respective host and between hosts. A hostmanager may be used by multiple backends at once, and a backend usually uses a large number of hosts to distribute elements.

The hostmanager provides the _hostmanager API_ to the backend.


## Backend and Webfrontend: Your Responsibilities

As testbed manager, it is your job to host an instance of the webfrontend and the backend services, as well as provide the required resources to your users.

The services are managed via [Docker](https://docker.com): Each service runs in its own container. It is your decision whether all services are located on the same server, or distributed over multiple ones. It is not difficult to migrate services, so you can change your mind later - for the beginning, one server should be more than sufficient to run the entire backend and webfrontend.

The roles of the required containers will be discussed here:


### Webfrontend

The webfrontend is a graphical user interface for ToMaTo. Internally, it makes use of the ToMaTo API, and is just one of many possible clients for ToMaTo. Except for temporary session data, it does not store any information on its own - every HTTP request is translated into one or multiple API calls.


### Database

The `db` module is the database of ToMaTo, running MongoDB. The other backend services are connected to this module.

Every backend module uses its own database, meaning that no data is shared between backend services in the database. When you distribute your backend over multiple servers, there should be one instance of the `db` module on each physical server.

The connections between the backend modules and the `db` module are realized via Docker, meaning that your database is not even exposed to your physical server (you can access it through docker, but not via network).


### Backend Core

The `backend_core` module contains the core functionality of ToMaTo. Its functionality is highly bound to each other which is why it hasn't been split into more parts yet, but this may happen in the future.

The responsibilities of `backend_core` are:

* Management of sites and hosts
* Management of topologies, elements, and connections
* Management of templates, profiles, and external networks
* Communication and synchronization with the hosts
* Collection and forwarding of accounting information from individual hosts


### Backend Users

The `backend_users` module manages users and organizations.


### Backend Accounting

The `backend_accounting` module manages quota data. It receives 1-minute-records for elements and connections from `backend_core` and aggregates them to longer periods, as well as to usage data for topologies, hosts, users, and organizations.

Due to the high demands on performance, this module is the only one that is not written in Python, but in a compiled language. On updates, the respective Docker container may re-compile the software, resulting in a short outage. However, ToMaTo is robust against unavailability of this module (although usage data may not be readable in such a case).


### Backend API

The `backend_api` module provides the ToMaTo API to the outside, and is responsible for authentication and authorization decisions. For this functionality, many information from the other modules, like element info or user info, is cached.


### Backend Debug

The `backend_debug` module collects internal debug information, most importantly, the [dump manager](../dumpmanager).

