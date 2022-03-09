#!/usr/bin/env python

"""Rename animes of a directory

USAGE:
======
    python media-file-organizer.py
"""

__authors__ = ("Julien POIROU")
__contributor__ = ("...")
__contact__ = ("poiroujulien@gmail.com")
__copyright__ = "MIT"
__date__ = "2022-03-09"
__version__ = "1.0.0"

import motd
import exit
import rename

import os
import datetime
import yaml
import sys

NAME = 'MediaConfigSync'
CONFIG = 'config.yaml'
ICON = 'icon.ico'
LOGS = 'information.log'

if __name__ == "__main__":
    motd.motd(__date__, __authors__, __contributor__, __version__)
    rename.renames(NAME, CONFIG, ICON, LOGS)
    exit.exit()