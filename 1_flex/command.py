#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		f" --docdir=/usr/share/doc/flex-{self.version}"
		 " --disable-static"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
	self.cmd_run("ln -sfv flex /usr/bin/lex")
	self.cmd_run("ln -sfv flex.1 /usr/share/man/man1/lex.1")
