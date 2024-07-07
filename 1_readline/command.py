#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.download_patch("readline-8.2-upstream_fixes-3")
	self.chroot()
	self.cmd_run(
		 "sed -i '/MV.*old/d' Makefile.in &&"
		 " sed -i '/{OLDSUFF}/c:' support/shlib-install"
	)
	self.apply_patch("readline-8.2-upstream_fixes-3", "-Np1")
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		 " --disable-static"
		 " --with-curses"
		f" --docdir=/usr/share/doc/readline-{self.version}"
	)

def compile(self):
	self.cmd_run("make SHLIB_LIBS='-lncursesw'")

def install(self):
	self.cmd_run(
		 "make SHLIB_LIBS='-lncursesw' install &&"
		 " install -v -m644 doc/*.{ps,pdf,html,dvi}"
		f" /usr/share/doc/readline-{self.version}"
	)
