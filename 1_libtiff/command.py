#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.take_build()
	self.cmd_run(
		 "cmake .. "
		f" -D CMAKE_INSTALL_DOCDIR={PREFIX}/share/doc/libtiff-{self.version}"
		f" -D CMAKE_INSTALL_PREFIX={PREFIX}"
		 " -G Ninja"
	)

def compile(self):
	self.cmd_run("ninja")

def check(self):
	self.cmd_run("ninja test")

def install(self):
	self.cmd_run("ninja install")
