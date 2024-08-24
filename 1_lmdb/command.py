#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	os.chdir("libraries/liblmdb")

def compile(self):
	self.cmd_run("make")
	self.cmd_run("sed -i 's| liblmdb.a||' Makefile")

def install(self):
	self.cmd_run(f"make prefix={PREFIX} install")
