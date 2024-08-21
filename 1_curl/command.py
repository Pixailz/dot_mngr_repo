#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		 " --disable-static"
		 " --with-openssl"
		 " --enable-threaded-resolver"
		 " --with-ca-path=/etc/ssl/certs"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install")
	self.cmd_run("rm -rf docs/examples/.deps")
	self.cmd_run(
		 "find docs \\( -name Makefile\\* -o"
		 " -name \\*.1 -o"
		 " -name \\*.3 -o"
		 " -name CMakeLists.txt \\) -delete"
	)
	self.cmd_run(f"cp -v -R docs -T /usr/share/doc/curl-{self.version}")
