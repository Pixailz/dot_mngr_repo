#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --sysconfdir=/etc"
		 " --localstatedir=/var"
		 " --disable-docs"
		f" --docdir={PREFIX}/share/doc/fontconfig-{self.version}"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(
		f"install -v -dm755 {PREFIX}/share/"
		 "{man/man{1,3,5},doc/fontconfig-" + self.version + "/fontconfig-devel}"
	)
	self.cmd_run(f"install -v -m644 fc-*/*.1 {PREFIX}/share/man/man1")
	self.cmd_run(f"install -v -m644 doc/*.3 {PREFIX}/share/man/man3")
	self.cmd_run(f"install -v -m644 doc/fonts-conf.5 {PREFIX}/share/man/man5")
	self.cmd_run(
		 "install -v -m644 doc/fontconfig-devel/*"
		f" {PREFIX}/share/doc/fontconfig-{self.version}/fontconfig-devel "
	)
	self.cmd_run(
		 "install -v -m644 doc/*.{pdf,sgml,txt,html}"
		f" {PREFIX}/share/doc/fontconfig-{self.version}"
	)