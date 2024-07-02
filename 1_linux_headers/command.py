#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.cmd_run("make mrproper")

def compile(self):
	self.cmd_run("make headers")

def check(self):
	pass

def install(self):
	self.cmd_run(
		 "find usr/include -type f ! -name '*.h' -delete &&"
		f" cp -r usr/include {PREFIX}/usr"
	)

def uninstall(self):
	pass
