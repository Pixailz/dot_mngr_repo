#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		f" --libexecdir={PREFIX}/lib"
		 " --with-secure-path"
		 " --with-env-editor"
		f" --docdir={PREFIX}/share/doc/sudo-{self.version}"
		 " --with-passprompt='[sudo] enter password for %p: '"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("env LC_ALL=C make check |& tee make-check.log")

def install(self):
	self.cmd_run("make install")
