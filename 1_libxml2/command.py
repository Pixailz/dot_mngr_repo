#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.generate_configure()

	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --sysconfdir=/etc"
		 " --disable-static"
		 " --with-history"
		 " --with-icu"
		f" PYTHON={PREFIX}/bin/python3"
		f" --docdir={PREFIX}/share/doc/libxml2-{self.version}"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install")
	self.cmd_run("rm -vf {PREFIX}/lib/libxml2.la")
	self.cmd_run(f"sed '/libs=/s/xml2.*/xml2\"/' -i {PREFIX}/bin/xml2-config")
