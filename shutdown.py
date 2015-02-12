#! /usr/bin/python
#coding=utf-8

import time
from os import system
running=True
while running:
	input=raw_input('shutdown(s) or reboot(r)? quit(q)')
	input=input.lower()
	if input=='q' or input=='quit':
		running=False
		print 'program quit'
		break
	seconds=int(raw_input("please enter the pause time(s):"))
	time.sleep(seconds)
	print 'pause time:',seconds
	running=False

	if input=='s':
	    print 'closing'
	    system('halt')
	elif input=='r':
	    print "rebooting"
	    system('reboot')
	else:
	    print "Error,Please enter again"
	    running=True
print 'program end'	            	