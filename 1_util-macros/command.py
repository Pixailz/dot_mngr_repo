#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		f" {XORG_CONFIG}"
	)

def install(self):
	self.cmd_run("make install")