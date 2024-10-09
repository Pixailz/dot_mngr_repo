#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run("sed -i -r 's:\"(/system):\"/org/gnome\\1:g' schemas/*.in")
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
