#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		f" --mandir={PREFIX}/share/man"
		 " --with-shared"
		 " --without-debug"
		 " --without-normal"
		 " --with-cxx-shared"
		 " --enable-pc-files"
		f" --with-pkg-config-libdir={PREFIX}/lib/pkgconfig"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run('make DESTDIR="${PWD}/dest" install')
	self.cmd_run(f"install -vm755 dest{PREFIX}/lib/libncursesw.so.{self.version} {PREFIX}/lib")
	self.cmd_run(f"rm -v  dest{PREFIX}/lib/libncursesw.so.{self.version}")
	self.cmd_run(f"sed -e 's/^#if.*XOPEN.*$/#if 1/' -i dest{PREFIX}/include/curses.h")
	self.cmd_run("cp -av dest/* /")
	self.cmd_run(
		 "for lib in ncurses form panel menu ; do"
		 " ln -sfv lib${lib}w.so " f"{PREFIX}" "/lib/lib${lib}.so &&"
		 " ln -sfv ${lib}w.pc " f"{PREFIX}" "/lib/pkgconfig/${lib}.pc; "
		 "done"
	)
	self.cmd_run(f"ln -sfv libncursesw.so {PREFIX}/lib/libcurses.so")
	self.cmd_run(f"cp -v -R doc -T {PREFIX}/share/doc/ncurses-{self.version}")
	self.cmd_run("make distclean")
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --with-shared"
		 " --without-normal"
		 " --without-debug"
		 " --without-cxx-binding"
		 " --with-abi-version=5"
	)
	self.cmd_run("make sources libs")
	self.cmd_run(f"cp -av lib/lib*.so.5* {PREFIX}/lib")
