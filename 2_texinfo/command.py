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
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(f"make TEXMF={PREFIX}/share/texmf install-tex")
	os.chdir(f"{PREFIX}/share/info")
	self.cmd_run("rm -fv dir")
	self.cmd_run("for f in * ; do install-info $f dir 2>/dev/null ; done")