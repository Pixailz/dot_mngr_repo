#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		 " --disable-static"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
	self.cmd_run("chmod -v 755 /usr/lib/lib{hogweed,nettle}.so")
	self.cmd_run(f"install -v -m755 -d /usr/share/doc/nettle-{self.version}")
	self.cmd_run(
		 "install -v -m644 nettle.{html,pdf}"
		f" /usr/share/doc/nettle-{self.version}"
	)
