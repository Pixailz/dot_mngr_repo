#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --enable-hashes=strong,glibc"
		 " --enable-obsolete-api=no"
		 " --disable-static"
		 " --disable-failure-tokens"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
	self.cmd_run("make distclean")
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --enable-hashes=strong,glibc"
		 " --enable-obsolete-api=glibc"
		 " --disable-static"
		 " --disable-failure-tokens"
	)
	self.cmd_run("make")
	self.cmd_run(f"cp -av --remove-destination .libs/libcrypt.so.1* {PREFIX}/lib")
