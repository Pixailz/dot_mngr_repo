#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		 " --sysconfdir=/etc"
		 " --runstatedir=/run"
		 " --without-logger"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install")
