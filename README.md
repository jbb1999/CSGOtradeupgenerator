SoCo
SoCo (Sonos Controller) is a Python library that allows you to control Sonos speakers programmatically. It was originally created at Music Hack Day Sydney by Rahim Sonawalla and is now developed by a team of people at its GitHub repository

For more background on the project, please see Rahim's blog post.

Visit the SoCo documentation for a more detailed overview of the functionailty.

Join the chat at https://gitter.im/SoCo/SoCo Build Status Requirements Status Latest PyPI version
WARNING
Sonos has changed the way music service account information is available. This means that currently a group of music service will give authentication issues and cannot be used at all. Known members of this group are: Google Play Music, Apple Music, Amazon Music, Spotify and Napster.

Issue #557 is a meta issue for this problem and you can use that to track progress on solving the issues, but please refrain from posting "me too" comments in there. Also, there is no need to open any more separate issue about this. If you have another music service that should be on the list, comment in #557

As of v0.26.0, nascent music service support has been reinstated, with some known issues. Testing and issue reporting would be appreciated.

Installation
SoCo requires Python 3.6 or newer.

Use pip:

pip install soco

SoCo depends on a number of Python packages. If you use pip to install Soco, the dependencies will be installed automatically for you. If not, you can inspect the requirements in the requirements.txt file.
