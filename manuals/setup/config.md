---
layout: manual
title: User Manual
manual: setup
manpage: config
category: manuals
---

# ToMaTo Configuration

The ToMaTo configuration requires two separate configuration files:

* `tomato-ctl.conf`, which sets up the individual [containers](../introduction), and
* `config.yaml`, which configures the ToMaTo modules.

## Config File Location

tomato-ctl.conf may be located at any of these directories:
* `/etc/tomato/`
* `~/.tomato/`
* the current working directory when executing tomato-ctl
* `~/ToMaTo/docker/run` (or where else the software is located)

{:.alert .alert-info}
The configuration file is read from all of these locations, in the respective order. If a value is set twice, the later one will have priority. Lists will be extended on conflict.

The location of config.yaml is defined in tomato-ctl.conf

## <a name="tomato-ctl.conf"></a>tomato-ctl.conf

`tomato-ctl.conf` defines the behavior of the [tomato-ctl tool](../tomato-ctl). This includes the selection of available ToMaTo modules on the host, docker container options like DNS server, and the selection of directories. Thus, this file depends on the host: if you distribute your ToMaTo services over multiple hosts, each host will have its individual `tomato-ctl.conf`. Although ToMaTo runs in a container, all data is stored on the host's hard disk.

For a detailed documentation, execute the tomato-ctl tool with the `help-config` command. You may need to read more about [container management](../tomato-ctl) to understand these options. The following will describe a quick setup.

`tomato-ctl.conf` is a JSON file consisting of sections for the individual ToMaTo modules' containers, as well as some global configuration options. You can skip all sections or options that you want to leave as default.

You should specify a `docker_dir` which should point to the directory that tomato-ctl is located in (usually `~/ToMaTo/docker/run`). You should also specify the location of `config.yaml` as `config.yaml_path`.

{% highlight json %}
{
	"docker_dir": "/home/yourusername/work/ToMaTo/docker/run",
	"config.yaml_path": "/home/yourusername/.tomato/config.yaml"
}
{% endhighlight %}

For example, to disable the webfrontend, add a `web` section to tomato-ctl.conf and overwrite the `enabled` property of it:
{% highlight json %}
"web": {
  "enabled": false
}
{% endhighlight %}

## <a name="config.yaml"></a>config.yaml

`config.yaml` is the central configuration file of the ToMaTo backend and webfrontend. This file should be shared between all ToMaTo modules. Contrary to `tomato-ctl.conf`, you must specify all options in `config.yaml` - if an option is missing, ToMaTo may select a default, or it may not start, depending on the importance of the option.

A default `config.yaml` is available at `~/ToMaTo/docker/run/config.yaml`. The following will describe the individual sections.

{:.alert .alert-info}
When reading config.yaml, ToMaTo first treats it as a format string and inserts system variables. So you can use a value like `%(OS_VAR)s` as a placeholder for the system variable `$OS_VAR`. All times are provided as seconds.

### services

This section describes the location of the individual ToMaTo services. When distributing ToMaTo over multiple hosts, you can set on which host each service is located. The respective hostnames must be [eindeutig] for all hosts. When using only one physicial host, the hostname `dockerhost`points to this host.

### web-url

This is a string pointing to the web root (without tailing `/`). It is used for display in the API, allowing clients to point to the respective webfrontend.

### external-urls

A list of URLs to external pages.

### github

ToMaTo's [dumpmanager](../dumpmanager) has the ability to open issues on GitHub. This section configures user and repository for this.

### backend_api

This section describes the technical configuration of the `backend_api` module in its container.

#### paths

Different paths on the system

#### dumps

Settings for dump collection

#### ssl

SSL settings

#### tasks

Settings for ToMaTo's internal task management.

### backend_accounting

This section describes the technical configuration of the `backend_accounting` module in its container.

#### data-path

Location of data

#### dumps

This is not supported on `backend_accounting`, and must thus be disabled.

### backend_core

This section describes the technical configuration of the `backend_core` module in its container.

#### paths

Different paths on the system

#### dumps

Settings for dump collection

#### ssl

SSL settings

#### database

Database connection settings

#### host-connections

Settings for the connections to hostmanagers

#### tasks

Settings for ToMaTo's internal task management.

### backend_users

This section describes the technical configuration of the `backend_users` module in its container.

#### paths

Different paths on the system

#### dumps

Settings for dump collection

#### ssl

SSL settings

#### database

Database connection settings

#### tasks

Settings for ToMaTo's internal task management.

### backend_debug

This section describes the technical configuration of the `backend_debug` module in its container.

#### paths

Different paths on the system

#### dumps

Settings for dump collection

#### ssl

SSL settings

#### database

Database connection settings

#### tasks

Settings for ToMaTo's internal task management.

### web

This section describes the technical configuration of the webfrontend in its container.

#### paths

Different paths on the system

#### dumps

Settings for dump collection

#### ssl

SSL settings

#### duration-log

The duration log is a log of the durations of the last 25 calls of each API function. This can be used to find performance problems, but can be disabled if you are not interested in this.

#### web-resources

Configuration of certain [resources](../resource). See this manual page for more information.

### rpc-timeout

timeout setting for API methods.

### email

Configuration for sending e-mails. Only important for the `backend_users` module.

### topologies

Topoloy timeout settings.

### user-quota

Set the user quota, i.e., the amount of usage a user may cause until they are blocked.

### dumpmanager

Configuration for the [dumpmanager](../dumpmanager). You should specify a better secret key which is shared between webfrontend and backend.

### debugging

Should only be enabled for software development.
