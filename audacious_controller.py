#!/usr/bin/env python

from os import system
import sys, tty
import alsaaudio


system('export DISPLAY=:0')
mixer=alsaaudio.Mixer()


def vol_inc(inc=10):
	init_vol=int(mixer.getvolume()[0])
	newvolume=init_vol+inc
	if newvolume >100 :
		newvolume=100
	mixer.setvolume(newvolume)

def vol_dec(dec=10):
	init_vol=int(mixer.getvolume()[0])
	newvolume=init_vol-dec
	if newvolume<0:
		newvolume=0
	mixer.setvolume(newvolume)


print("Press 'P' for pause/play, 'N' for next song, 'R' for previous and 'S' to stop, 'Z' to decrease volume and 'X' to increase")

tty.setcbreak(sys.stdin)
while True:
	a=ord(sys.stdin.read(1))
	if (a==80) | (a==112):
		system('audacious -t')
	elif (a==78) | (a==110):
		system('audacious -f')
	elif (a==82) | (a==114):
		system('audacious -r')
	elif (a==83) | (a==115):
		system('audacious -s')
	elif (a==122) | (a==90):
		vol_dec()
	elif (a==120) | (a==88):
		vol_inc()
	elif a==27:
		sys.exit(0)
