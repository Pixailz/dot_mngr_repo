#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.download_patch("sysvinit-3.10-consolidated-1")
	self.chroot()
	self.apply_patch("sysvinit-3.10-consolidated-1", "-Np1")

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install")
