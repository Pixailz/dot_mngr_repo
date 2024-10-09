#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		f" --docdir={PREFIX}/share/doc/pcre2-{self.version}"
		 " --enable-unicode"
		 " --enable-jit"
		 " --enable-pcre2-16"
		 " --enable-pcre2-32"
		 " --enable-pcre2grep-libz"
		 " --enable-pcre2grep-libbz2"
		 " --enable-pcre2test-libreadline"
		 " --disable-static"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")