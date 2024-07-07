#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		"""python3 -c 'from pty import spawn; spawn(["echo", "okey"])' | grep okey"""
	)
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		 " --with-tcl=/usr/lib"
		 " --enable-shared"
		 " --mandir=/usr/share/man"
		 " --with-tclinclude=/usr/include"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make test")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(f"ln -svf expect{self.version}/libexpect{self.version}.so /usr/lib")
