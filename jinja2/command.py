#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()

def compile(self):
	self.cmd_run(
		 "pip3 wheel"
		 " -w dist"
		 " --no-cache-dir"
		 " --no-build-isolation"
		 " --no-deps"
		 " ${PWD}"
	)

def install(self):
	self.cmd_run(
		 "pip3 install"
		 " --no-index"
		 " --no-user"
		 " --find-links dist"
		 " Jinja2"
	)
