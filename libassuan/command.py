#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
	)

def compile(self):
	self.cmd_run("make")
	self.cmd_run("make -C doc html")
	self.cmd_run("makeinfo --html --no-split -o doc/assuan_nochunks.html doc/assuan.texi")
	self.cmd_run("makeinfo --plaintext -o doc/assuan.txt doc/assuan.texi")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(f"install -v -dm755 /usr/share/doc/libassuan-{self.version}/html")
	self.cmd_run(
		 "install -v -m644 doc/assuan.html/*"
		f" /usr/share/doc/libassuan-{self.version}/html"
	)
	self.cmd_run(
		 "install -v -m644 doc/assuan_nochunks.html"
		f" /usr/share/doc/libassuan-{self.version}"
	)
	self.cmd_run(
		 "install -v -m644 doc/assuan.{txt,texi}"
		f" /usr/share/doc/libassuan-{self.version}"
	)
