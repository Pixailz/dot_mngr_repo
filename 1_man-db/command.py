#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		f" --docdir={PREFIX}/share/doc/man-db-{self.version}"
		 " --sysconfdir=/etc"
		 " --disable-setuid"
		 " --enable-cache-owner=bin"
		f" --with-browser={PREFIX}/bin/lynx"
		f" --with-vgrind={PREFIX}/bin/vgrind"
		f" --with-grap={PREFIX}/bin/grap"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
