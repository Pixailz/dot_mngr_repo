#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		 " --disable-shared"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run(
		 "cp -v gettext-tools/src/{msgfmt,msgmerge,xgettext} "
		f"{PREFIX}/bin"
	)
