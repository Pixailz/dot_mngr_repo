#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --sysconfdir=/etc"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
