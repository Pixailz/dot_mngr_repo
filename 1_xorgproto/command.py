#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.take_build()
	self.cmd_run(
		 "meson setup .."
		f" --prefix={XORG_PREFIX}"
	)

def compile(self):
	self.cmd_run("ninja")

def install(self):
	self.cmd_run("ninja install")
	self.cmd_run(f"rm -f {XORG_PREFIX}/lib/pkgconfig/xcb-proto.pc")
