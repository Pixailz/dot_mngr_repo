#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run("sed -i '/install.*libaio.a/s/^/#/' src/Makefile")

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make partcheck")

def install(self):
	self.cmd_run("make install")
