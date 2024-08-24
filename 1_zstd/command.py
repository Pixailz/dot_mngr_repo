#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()

def compile(self):
	self.cmd_run(f"make prefix={PREFIX}")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run(f"make prefix={PREFIX} install")
	self.cmd_run(f"rm -fv {PREFIX}/lib/libzstd.a")
