#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.download_patch("unzip-6.0-consolidated-1")
	self.download_patch("unzip-6.0-gcc14-1")
	self.chroot()
	self.apply_patch("unzip-6.0-consolidated-1", "-Np1")
	self.apply_patch("unzip-6.0-gcc14-1", "-Np1")

def compile(self):
	self.cmd_run("make -f unix/Makefile generic")

def install(self):
	self.cmd_run(
		 "make"
		f" prefix={PREFIX}"
		f" MANDIR={PREFIX}/share/man/man1"
		 " -f unix/Makefile install"
	)
