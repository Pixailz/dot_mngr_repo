#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "FORCE_UNSAFE_CONFIGURE=1 ./configure"
		 " --prefix=/usr"
	)

def compile(self):
	self.cmd_run("make")

# def check(self):
# 	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(f"make -C doc install-html docdir=/usr/share/doc/tar-{self.version}")
