#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.take_build()
	self.cmd_run(
		 "../configure"
		f" --prefix={PREFIX}"
		 " --disable-gpg-test"
	)

def compile(self):
	self.cmd_run("make PYTHONS=")

def install(self):
	self.cmd_run("make install PYTHONS=")
