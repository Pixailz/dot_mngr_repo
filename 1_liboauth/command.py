#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.download_patch("liboauth-1.0.3-openssl-1.1.0-3")
	self.chroot()
	self.apply_patch("liboauth-1.0.3-openssl-1.1.0-3", "-Np1")
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --disable-static"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
