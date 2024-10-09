#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "PYTHON=python3"
		 " ./configure"
		f" {XORG_CONFIG}"
	)

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
