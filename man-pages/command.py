#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run("rm -v man3/crypt*")

def install(self):
	self.cmd_run("make prefix=/usr install")
