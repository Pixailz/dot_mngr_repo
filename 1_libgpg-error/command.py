#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(f"install -v -m644 -D README {PREFIX}/share/doc/libgpg-error-{self.version}/README")