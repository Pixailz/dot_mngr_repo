#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.take_build()
	self.cmd_run(
		 "../configure"
		 " --prefix=/usr"
		 " --localstatedir=/var"
		 " --sysconfdir=/etc"
		f" --docdir=/usr/share/doc/gnupg-{self.version}"
	)

def compile(self):
	self.cmd_run("make")
	self.cmd_run("makeinfo --html --no-split -I doc -o doc/gnupg_nochunks.html ../doc/gnupg.texi")
	self.cmd_run("makeinfo --plaintext -I doc -o doc/gnupg.txt ../doc/gnupg.texi")
	self.cmd_run("make -C doc html")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(f"install -v -m755 -d /usr/share/doc/gnupg-{self.version}/html")
	self.cmd_run(f"install -v -m644 doc/gnupg_nochunks.html /usr/share/doc/gnupg-{self.version}/html/gnupg.html")
	self.cmd_run(f"install -v -m644 ../doc/*.texi doc/gnupg.txt /usr/share/doc/gnupg-{self.version}")
	self.cmd_run(f"install -v -m644 doc/gnupg_nochunks.html /usr/share/doc/gnupg-{self.version}/html/gnupg.html")
	self.cmd_run(f"install -v -m644 doc/gnupg.html/* /usr/share/doc/gnupg-{self.version}/html")
