#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.add_path(f"{PREFIX}/tools/bin")
	self.take_build()
	self.cmd_run(
		 "../configure"
		f" --prefix={PREFIX}/tools"
		f" --with-sysroot={PREFIX}"
		f" --target={TARGET_TRIPLET}"
		 " --disable-nls"
		 " --disable-werror"
		 " --enable-gprofng=no"
		 " --enable-default-hash-style=gnu", 1
	)

def compile(self):
	self.cmd_run("make", 1)

def install(self):
	self.cmd_run("make install", 1)
