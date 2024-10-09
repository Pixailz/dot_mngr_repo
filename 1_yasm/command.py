#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run("sed -i 's#) ytasm.*#)#' Makefile.in")
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make check", 1)

def install(self):
	self.cmd_run("make install")