#!/bin/bash

# This is for KDE. If you dont use KDE, please configure accordingly
while pgrep "kscreenlocker"; do
  python3 login.py
  break
done