#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./config"
		 " --prefix=/usr"
		 " --openssldir=/etc/ssl"
		 " --libdir=/lib"
		 " shared zlib-dynamic"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run(f"HARNESS_JOBS={NB_PROC} make test")

def install(self):
	self.cmd_run("sed -i '/INSTALL_LIBS/s/libcrypto.a libssl.a//' Makefile")
	self.cmd_run("make MANSUFFIX=ssl install")
	self.cmd_run(f"mv -v /usr/share/doc/openssl /usr/share/doc/openssl-{self.version}")
	self.cmd_run(f"cp -vfr doc/* /usr/share/doc/openssl-{self.version}")
