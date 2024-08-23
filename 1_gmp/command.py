#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		f"./configure"
		 " --prefix=/usr"
		 " --enable-cxx"
		 " --disable-static"
		f" --docdir=/usr/share/doc/gmp-{self.version}"
	)

def compile(self):
	self.cmd_run("make")
	self.cmd_run("make html")

def check(self):
	self.cmd_run("make check 2>&1 | tee gmp-check-log || true")
	self.cmd_run("awk '/# PASS:/{total+=$3} ; END{print total}' gmp-check-log")

def install(self):
	self.cmd_run(f"make install")
	self.cmd_run(f"make install-html")
