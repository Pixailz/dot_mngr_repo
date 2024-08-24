#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.take_build()
	self.cmd_run(
		 "../configure"
		f" --prefix={PREFIX}"
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
	self.cmd_run(f"make tooldir={PREFIX}")

# def check(self):
# 	self.cmd_run("make -k check")

def install(self):
	self.cmd_run(f"make tooldir={PREFIX} install")
	self.cmd_run(
		f"rm -fv {PREFIX}"
		"/lib/lib{bfd,ctf,ctf-nobfd,gprofng,opcodes,sframe}.a"
	)
