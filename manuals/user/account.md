---
layout: manual
title: User Manual
manual: user
manpage: account
category: manuals
---

# Your User Account

Your personal user account is your key to all your experiments on the ToMaTo testbed. All data you store or generate during your experiments can be accessed by your user account.

{:.alert .alert-info}
You should not share your user account with other people. Instead, every person should have their own account. [Topologies can be shared between multiple users.](../topology/permission)


## Registering

If your organization does not participate in the ToMaTo consortium, it must [register for it](/join).

If you do not have an own user account, you can register for a new account [here](https://master.tomato-lab.org/account/register). Upon registration, you will need to select an account name which will be used for identifying you. To protect your account, you should select a strong password. Once you have been registered, an administrator of your organization will activate your account.

If you have not talked to any administrator before registering, you should provide a _Reason for Registering_. This is an optional message which is sent to all administrators when you register.

If your account has not been activated, you have still access to the testbed, but you cannot occupy testbed resources. This means that you can design [topologies](../topology), but not [start](../element/action#start) them.


## Log-in and log-out

If you have access to an account, you can log in to ToMaTo. To do so, click on the "Login" button on the top-right corner of any page in the ToMaTo testbed. Alternatively, a log-in prompt will automatically appear when trying to access any protected page.

To quit your user session, click on your name in the top-right corner of the page, and select "Log Out".


## <a name="quota"></a>Quota

Usage of ToMaTo is subject to a quota restriction, meaning that you cannot prepare or start any new elements once you have exceeded a certain amount of CPU time, memory usage, disk usage, or network traffic. Normally, you should not exceed this if your experiments are not too expensive.

If you exceed your quota, you must contact your administrator for further actions. Your administrator can also disable quota restrictions in case you need to run an expensive experiment.

You can view your resource usage on your [account page](#your_account). Every topology, and every [element](../element) or [connection](../connection) in one of your topologies, has its own _Resource usage_ statistics.


## Notifications

ToMaTo will send you notifications - both via its internal notification system and via e-mail. The number of notifications is indicated via a number in the top-right corner of the page, next to your name. If there is at least one notification, the button will be highlighted in blue. To view notifications, click on this number.

{:.alert .alert-info}
You can disable e-mail notifications by setting the _NoMails_ flag in your account settings.

On the notifications page, you can mark notifications as read using the respective button. If you have more than one notification, there will be a button to mark all read on the bottom of the page. You can view read notifications, and even mark them as unread, by clicking on "Show All Notifications" on the top of the page.


## <a name="your_account"></a>Managing your account

To manage your account, log in to ToMaTo, click on your name in the top-right corner of the page, and select "My Account". [→ go now](https://master.tomato-lab.org/account)

On your account page, you can view your account settings, view statistics about your resource usage, edit your account information, reset your password, or completely remove your account.

_Flags_ are a mix of permissions and settings. As a normal user, the only interesting thing for you is 
