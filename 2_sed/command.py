#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
	)

def compile(self):
	self.cmd_run("make")
	self.cmd_run("make html")

def check(self):
	self.cmd_run("chown -R tester .")
	self.cmd_run("su tester -c 'PATH=${PATH} make check'")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(f"install -d -m755 {PREFIX}/share/doc/sed-{self.version}")
	self.cmd_run(f"install -m644 doc/sed.html {PREFIX}/share/doc/sed-{self.version}")
