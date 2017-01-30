---
layout: manual
title: User Manual
manual: user
manpage: element/template
category: manuals
---

# Templates

Templates are the initial [disk images](../image) for [devices](..).

## Available Templates

To see a list of available templates, click on _Templates_ under _Resources_ in the main menu. [](https://master.tomato-lab.org/template/) The list of templates contains the most important information, and you can see more information about a template by hovering your mouse over the icons in the right column. To see even more information about templates, you can click on the template's name.

Some templates are limited due to copyright. To get access to them, you have to ask your administrator.

## Determine a Device's Template

A device's template is shown in its config menu.

## Select template

The [editor's menu](../../topology/editor#men) includes a list of available templates in its _Devices_ and _Network_ tabs. Most devices in there are identical except for their template.

You can change the template anytime while your device is not started. The template can be selected in the device's config menu, or by right-clicking on the target element, open the _Disk Image_ submenu, and select _Change template_.

{:.alert .alert-warning}
Changing the template of a _prepared_ device will delete all existing data on the device's current disk image.
