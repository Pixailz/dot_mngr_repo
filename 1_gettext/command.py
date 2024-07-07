#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		f" --docdir=/usr/share/doc/gettext-{self.version}"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install")