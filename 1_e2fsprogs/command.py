#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.take_build()
	self.cmd_run(
		 "../configure"
		 " --prefix=/usr"
		 " --sysconfdir=/etc"
		 " --enable-elf-shlibs"
		 " --disable-libblkid"
		 " --disable-libuuid"
		 " --disable-uuidd"
		 " --disable-fsck"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
	self.cmd_run("rm -fv /usr/lib/{libcom_err,libe2p,libext2fs,libss}.a")
	self.cmd_run("gunzip -v /usr/share/info/libext2fs.info.gz")
	self.cmd_run("install-info --dir-file=/usr/share/info/dir /usr/share/info/libext2fs.info")
	self.cmd_run("makeinfo -o doc/com_err.info ../lib/et/com_err.texinfo")
	self.cmd_run("install -v -m644 doc/com_err.info /usr/share/info")
	self.cmd_run("install-info --dir-file=/usr/share/info/dir /usr/share/info/com_err.info")
