#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		 " --psfdir=/usr/share/consolefonts"
	)

def compile(self):
	self.cmd_run("make psf")

def install(self):
	self.cmd_run("make install-psf")