#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.take_build()
	self.cmd_run(
		 "meson setup .."
		f" --prefix={PREFIX}"
		 " --buildtype=release"
	)

def compile(self):
	self.cmd_run("meson compile")

def check(self):
	self.cmd_run("meson test --print-errorlogs --no-rebuild")

def install(self):
	self.cmd_run("meson install --no-rebuild")
