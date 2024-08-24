#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --disable-debuginfod"
		 " --enable-libdebuginfod=dummy"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make -C libelf install")
	self.cmd_run(f"install -vm644 config/libelf.pc {PREFIX}/lib/pkgconfig")
	self.cmd_run(f"rm {PREFIX}/lib/libelf.a")
