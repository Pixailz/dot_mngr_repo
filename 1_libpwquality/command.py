#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --disable-static"
		f" --with-securedir={PREFIX}/lib/security"
		 " --disable-python-bindings"
	)

def compile(self):
	self.cmd_run("make")
	self.cmd_run(
		 "pip3 wheel -w dist --no-build-isolation --no-deps --no-cache-dir"
		 " ${PWD}/python"
	)

def install(self):
	self.cmd_run("make install")
	self.cmd_run("pip3 install --no-index --find-links=dist --no-cache-dir --no-user pwquality")
