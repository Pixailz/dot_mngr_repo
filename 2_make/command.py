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

def check(self):
	self.cmd_run("chown -R tester .")
	self.cmd_run('su tester -c "PATH=${PATH} make check"')

def install(self):
	self.cmd_run("make install")
