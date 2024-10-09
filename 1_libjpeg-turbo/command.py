#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.take_build()
	self.cmd_run(
		 "cmake .."
		f" -D CMAKE_INSTALL_PREFIX={PREFIX}"
		 " -D CMAKE_BUILD_TYPE=RELEASE"
		 " -D ENABLE_STATIC=FALSE"
		 " -D CMAKE_INSTALL_DEFAULT_LIBDIR=lib"
		 " -D CMAKE_SKIP_INSTALL_RPATH=ON"
		f" -D CMAKE_INSTALL_DOCDIR={PREFIX}/share/doc/libjpeg-turbo-{self.version}"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make test")

def install(self):
	self.cmd_run("make install")