#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --disable-static"
		f" --docdir={PREFIX}/share/doc/pkgconf-{self.version}"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(f"ln -sfv pkgconf {PREFIX}/bin/pkg-config")
	self.cmd_run(f"ln -sfv pkgconf.1 {PREFIX}/share/man/man1/pkg-config.1")
