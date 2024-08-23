#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.take_build()
	self.cmd_run(
		 "../configure"
		 " --prefix=/usr"
		 " --sysconfdir=/etc"
		 " --enable-gold"
		 " --enable-ld=default"
		 " --enable-plugins"
		 " --enable-shared"
		 " --disable-werror"
		 " --enable-64-bit-bfd"
		 " --enable-new-dtags"
		 " --with-system-zlib"
		 " --enable-default-hash-style=gnu"
	)

def compile(self):
	self.cmd_run("make tooldir=/usr")

def check(self):
	self.cmd_run("make -k check")

def install(self):
	self.cmd_run(f"make tooldir=/usr install")
	self.cmd_run("rm -fv /usr/lib/lib{bfd,ctf,ctf-nobfd,gprofng,opcodes,sframe}.a")
