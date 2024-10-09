#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run("sed -i 's/-Os/-O2/' Makefile.sharedlibrary")

def compile(self):
	self.cmd_run(f"make -f Makefile.sharedlibrary INSTALL_PREFIX={PREFIX}")

def install(self):
	self.cmd_run(f"make -f Makefile.sharedlibrary INSTALL_PREFIX={PREFIX} install")