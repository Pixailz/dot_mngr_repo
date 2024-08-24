#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()

def compile(self):
	self.cmd_run(f"make BUILD_STATIC=no PREFIX={PREFIX}")

def check(self):
	self.cmd_run("make check", 1)

def install(self):
	self.cmd_run(f"make BUILD_STATIC=no PREFIX={PREFIX} install")
