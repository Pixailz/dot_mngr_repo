#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		f" --docdir={PREFIX}/share/doc/gnutls-{self.version}"
		 ' --with-default-trust-store-pkcs11="pkcs11:"'
	)

def compile(self):
	self.cmd_run("make")

# def check(self):
# 	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
