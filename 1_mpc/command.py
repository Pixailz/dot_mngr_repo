#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		f"./configure"
		f" --prefix={PREFIX}"
		 " --disable-static"
		f" --docdir={PREFIX}/share/doc/mpc-{self.version}"
	)

def compile(self):
	self.cmd_run("make")
	self.cmd_run("make html")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run(f"make install")
	self.cmd_run(f"make install-html")
