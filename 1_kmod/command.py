#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --sysconfdir=/etc"
		 " --with-openssl"
		 " --with-xz"
		 " --with-zstd"
		 " --with-zlib"
         " --disable-manpages"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(
		 "for target in depmod insmod modinfo modprobe rmmod; do"
		f" ln -sfv ../bin/kmod {PREFIX}/sbin/$target;"
		f" rm -fv {PREFIX}/bin/$target;"
		 " done"
	)
	self.cmd_run(f"ln -sfv kmod {PREFIX}/bin/lsmod")
