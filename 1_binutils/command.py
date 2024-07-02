#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.take_build()
	self.cmd_run(
		f"../configure --prefix={PREFIX}/tools"
		f" --with-sysroot={PREFIX}"
		f" --target={TARGET_TRIPLET}"
		 " --disable-nls"
		 " --disable-werror"
		 " --enable-gprofng=no"
		 " --enable-default-hash-style=gnu", 1
	)

def compile(self):
	self.cmd_run("make", 1)

def check(self):
	pass

def install(self):
	self.cmd_run("make install", 1)

def uninstall(self):
	pass
