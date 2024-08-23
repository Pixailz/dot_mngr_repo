#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		 " --disable-static"
		 " --without-nettle"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("LC_ALL=C make check")

def install(self):
	self.cmd_run("make install")
