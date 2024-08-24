#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	# self.download_patch("readline-8.2-upstream_fixes-3")
	self.chroot()
	self.cmd_run(
		 "sed -i '/MV.*old/d' Makefile.in &&"
		 " sed -i '/{OLDSUFF}/c:' support/shlib-install"
	)
	self.cmd_run("sed -i 's/-Wl,-rpath,[^ ]*//' support/shobj-conf")
	# self.apply_patch("readline-8.2-upstream_fixes-3", "-Np1")
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --disable-static"
		 " --with-curses"
		f" --docdir={PREFIX}/share/doc/readline-{self.version}"
	)

def compile(self):
	self.cmd_run("make SHLIB_LIBS='-lncursesw'")

def install(self):
	self.cmd_run("make SHLIB_LIBS='-lncursesw' install")
	self.cmd_run(
		 " install -v -m644 doc/*.{ps,pdf,html,dvi}"
		f" {PREFIX}/share/doc/readline-{self.version}"
	)
