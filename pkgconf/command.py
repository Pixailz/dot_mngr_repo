#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		 " --disable-static"
		f" --docdir=/usr/share/doc/pkgconf-{self.version}"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install")
	self.cmd_run("ln -sfv pkgconf /usr/bin/pkg-config")
	self.cmd_run("ln -sfv pkgconf.1 /usr/share/man/man1/pkg-config.1")
