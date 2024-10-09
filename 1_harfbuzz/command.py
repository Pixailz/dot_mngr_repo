#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.take_build()
	self.cmd_run(
		 "meson setup .."
		f" --prefix={PREFIX}"
		 " --buildtype=release"
		 " -D graphite2=enable"
	)

def compile(self):
	self.cmd_run("ninja")

def check(self):
	self.cmd_run("ninja test")

def install(self):
	self.cmd_run("ninja install")