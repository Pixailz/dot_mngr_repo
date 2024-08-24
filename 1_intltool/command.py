#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run("sed -i 's:\\\\\\${:\\\\\\$\\\\{:' intltool-update.in")
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(f"install -v -Dm644 doc/I18N-HOWTO {PREFIX}/share/doc/intltool-{self.version}/I18N-HOWTO")
