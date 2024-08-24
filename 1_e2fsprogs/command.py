#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.take_build()
	self.cmd_run(
		 "../configure"
		f" --prefix={PREFIX}"
		 " --sysconfdir=/etc"
		 " --enable-elf-shlibs"
		 " --disable-libblkid"
		 " --disable-libuuid"
		 " --disable-uuidd"
		 " --disable-fsck"
	)

def compile(self):
	self.cmd_run("make")

# def check(self):
# 	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(f"rm -fv {PREFIX}/lib/""{libcom_err,libe2p,libext2fs,libss}.a")
	self.cmd_run(f"gunzip -v {PREFIX}/share/info/libext2fs.info.gz")
	self.cmd_run(f"install-info --dir-file={PREFIX}/share/info/dir {PREFIX}/share/info/libext2fs.info")
	self.cmd_run("makeinfo -o doc/com_err.info ../lib/et/com_err.texinfo")
	self.cmd_run(f"install -v -m644 doc/com_err.info {PREFIX}/share/info")
	self.cmd_run(f"install-info --dir-file={PREFIX}/share/info/dir {PREFIX}/share/info/com_err.info")
