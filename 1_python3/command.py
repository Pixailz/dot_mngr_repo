#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --enable-shared"
		 " --without-ensurepip"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install")
