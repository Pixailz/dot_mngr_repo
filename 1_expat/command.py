#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --disable-static"
		f" --docdir={PREFIX}/share/doc/expat-{self.version}"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(
		 "install -v -m644 doc/*.{html,css}"
		f" {PREFIX}/share/doc/expat-{self.version}"
	)
