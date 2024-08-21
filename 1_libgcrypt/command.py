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
	self.cmd_run("makeinfo --html --no-split -o doc/gcrypt_nochunks.html doc/gcrypt.texi")
	self.cmd_run("makeinfo --plaintext -o doc/gcrypt.txt doc/gcrypt.texi")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(f"install -v -dm755 /usr/share/doc/libgcrypt-{self.version}")
	self.cmd_run(
		 "install -v -m644    README doc/{README.apichanges,fips*,libgcrypt*}"
		f" /usr/share/doc/libgcrypt-{self.version}"
	)
	self.cmd_run(f"install -v -dm755 /usr/share/doc/libgcrypt-{self.version}/html")
	self.cmd_run(
		 "install -v -m644 doc/gcrypt.html/*"
		f" /usr/share/doc/libgcrypt-{self.version}/html"
	)
	self.cmd_run(
		 "install -v -m644 doc/gcrypt_nochunks.html"
		f" /usr/share/doc/libgcrypt-{self.version}"
	)
	self.cmd_run(
		 "install -v -m644 doc/gcrypt.{txt,texi}"
		f" /usr/share/doc/libgcrypt-{self.version}"
	)
