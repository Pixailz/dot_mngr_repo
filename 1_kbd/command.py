#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.download_patch("kbd-2.6.4-backspace-1")
	self.chroot()
	self.apply_patch("kbd-2.6.4-backspace-1", "-Np1")
	self.cmd_run("sed -i '/RESIZECONS_PROGS=/s/yes/no/' configure")
	self.cmd_run("sed -i 's/resizecons.8 //' docs/man/man8/Makefile.in")
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --disable-vlock"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(f"cp -R -v docs/doc -T {PREFIX}/share/doc/kbd-{self.version}")
