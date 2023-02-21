#!/usr/bin/env python

from os import system
import sys, tty
import alsaaudio


system("export DISPLAY=:0")
mixer = alsaaudio.Mixer()


def vol_inc(inc=10):
    init_vol = int(mixer.getvolume()[0])
    newvolume = init_vol + inc
    if newvolume > 100:
        newvolume = 100
    mixer.setvolume(newvolume)


def vol_dec(dec=10):
    init_vol = int(mixer.getvolume()[0])
    newvolume = init_vol - dec
    if newvolume < 0:
        newvolume = 0
    mixer.setvolume(newvolume)

def play():
    system('audacious -t')
    
# add play, pause, next song, previous song, stop
# audacious -t, -f, -r, -s
# C:\Program Files (x86)\Audacious\bin\audacious.exe