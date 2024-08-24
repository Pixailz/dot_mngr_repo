#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.take_build()
	self.cmd_run(
		 "../configure"
		f" --prefix={PREFIX}"
	)

def compile(self):
	self.cmd_run("makeinfo --html --no-split -o doc/dejagnu.html ../doc/dejagnu.texi")
	self.cmd_run("makeinfo --plaintext -o doc/dejagnu.txt ../doc/dejagnu.texi")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(f"install -v -dm755 {PREFIX}/share/doc/dejagnu-{self.version}")
	self.cmd_run(
		 "install -v -m644 doc/dejagnu.{html,txt}"
		f" {PREFIX}/share/doc/dejagnu-{self.version}"
	)
