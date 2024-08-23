#!/usr/bin/env python3

from dot_mngr import *

def install(self):
	self.chroot()
	self.cmd_run("cp services protocols /etc")
