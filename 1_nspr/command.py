#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	Os.take("nspr")
	self.cmd_run("sed -i '/^RELEASE/s|^|#|' pr/src/misc/Makefile.in")
	self.cmd_run("sed -i 's|$(LIBRARY) ||'  config/rules.mk")
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --with-mozilla"
		 " --with-pthreads"
		f" $([ {ARCH} == 'x86_64' ] && echo --enable-64bit)"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install")
