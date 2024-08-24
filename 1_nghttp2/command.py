#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --disable-static"
		 " --enable-lib-only"
		f" --docdir={PREFIX}/share/doc/nghttp2-{self.version}"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install")
