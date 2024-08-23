#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		f" --docdir=/usr/share/doc/man-db-{self.version}"
		 " --sysconfdir=/etc"
		 " --disable-setuid"
		 " --enable-cache-owner=bin"
		 " --with-browser=/usr/bin/lynx"
		 " --with-vgrind=/usr/bin/vgrind"
		 " --with-grap=/usr/bin/grap"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
