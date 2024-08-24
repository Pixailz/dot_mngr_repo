#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
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
	self.cmd_run(f"chmod -v 755 {PREFIX}" "/lib/lib{hogweed,nettle}.so")
	self.cmd_run(f"install -v -m755 -d {PREFIX}/share/doc/nettle-{self.version}")
	self.cmd_run(
		 "install -v -m644 nettle.{html,pdf}"
		f" {PREFIX}/share/doc/nettle-{self.version}"
	)
