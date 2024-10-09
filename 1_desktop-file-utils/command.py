#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(f"rm -fv {PREFIX}/bin/desktop-file-edit")
	self.take_build()
	self.cmd_run(
		 "meson setup .."
		f" --prefix={PREFIX}"
		 " --buildtype=release"
	)

def compile(self):
	self.cmd_run("ninja")

def install(self):
	self.cmd_run("ninja install")