#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	download_package(self, "libpng-apng")
	self.chroot()
	libpng_apng_patchs = conf.get_package("libpng-apng")
	self.cmd_run(
		 "gzip -cd" +
		 self.chrooted_get_path(libpng_apng_patchs.file_path, self.chrooted) +
		 " | patch -p1"
	)
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --disable-static"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(f"mkdir -v {PREFIX}/share/doc/libpng-{self.version}")
	self.cmd_run(
		 "cp -v README libpng-manual.txt"
		f" {PREFIX}/share/doc/libpng-{self.version}"
	)
