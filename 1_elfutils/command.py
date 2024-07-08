#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		 " --disable-debuginfod"
		 " --enable-libdebuginfod=dummy"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make -C libelf install")
	self.cmd_run("install -vm644 config/libelf.pc /usr/lib/pkgconfig")
	self.cmd_run("rm /usr/lib/libelf.a")
