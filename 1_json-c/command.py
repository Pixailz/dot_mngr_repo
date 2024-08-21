#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.take_build()
	self.cmd_run(
		 "cmake"
		 " -DCMAKE_INSTALL_PREFIX=/usr"
		 " -DCMAKE_BUILD_TYPE=Release"
		 " -DBUILD_STATIC_LIBS=OFF"
		 " .."
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make test")

def install(self):
	self.cmd_run("make install")
	# self.cmd_run(f"install -d -vm755 /usr/share/doc/json-c-{self.version}")
	# self.cmd_run(f"install -v -m644 ../doc/html/* /usr/share/doc/json-c-{self.version}")
