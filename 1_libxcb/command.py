#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure "
		f" {XORG_CONFIG}"
		 " --without-doxygen"
		 " --docdir='${datadir}'/doc/libxcb-"
		f"{self.version}"
	)

def compile(self):
	self.cmd_run("LC_ALL=en_US.UTF-8 make")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(
		f"chown -Rv root:root {XORG_PREFIX}/share/doc/libxcb-{self.version}"
	)
