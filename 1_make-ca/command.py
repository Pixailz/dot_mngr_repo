#!/usr/bin/env python3

from dot_mngr import *

def install(self):
	self.chroot()
	self.cmd_run("make install")
	self.cmd_run("install -vdm755 /etc/ssl/local")
