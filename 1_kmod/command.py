#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		 " --sysconfdir=/etc"
		 " --with-openssl"
		 " --with-xz"
		 " --with-zstd"
		 " --with-zlib"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(
		 "for target in depmod insmod modinfo modprobe rmmod; do"
		 " ln -sfv ../bin/kmod /usr/sbin/$target;"
		 " done"
	)
	self.cmd_run("ln -sfv kmod /usr/bin/lsmod")
