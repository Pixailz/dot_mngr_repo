#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run("sed -i '/LIBPOSTFIX=\"64\"/s/64//' configure.ac")
	self.cmd_run("./autogen.sh")
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		f" --docdir={PREFIX}/share/doc/graphviz-{self.version}"
	)
	self.cmd_run('sed -i "s/0/$(date +%Y%m%d)/" builddate.h')

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install")