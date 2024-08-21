#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	if not os.path.exists("configure"):
		self.cmd_run("sh autogen.sh")
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		 " --sysconfdir=/etc"
		 " --disable-static"
		 " --with-history"
		 " --with-icu"
		 " PYTHON=/usr/bin/python3"
		f" --docdir=/usr/share/doc/libxml2-{self.version}"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install")
	self.cmd_run("rm -vf /usr/lib/libxml2.la")
	self.cmd_run("sed '/libs=/s/xml2.*/xml2\"/' -i /usr/bin/xml2-config")
