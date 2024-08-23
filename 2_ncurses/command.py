#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		 " --mandir=/usr/share/man"
		 " --with-shared"
		 " --without-debug"
		 " --without-normal"
		 " --with-cxx-shared"
		 " --enable-pc-files"
		 " --with-pkg-config-libdir=/usr/lib/pkgconfig"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run('make DESTDIR="${PWD}/dest" install')
	self.cmd_run(f"install -vm755 dest/usr/lib/libncursesw.so.{self.version} /usr/lib")
	self.cmd_run(f"rm -v  dest/usr/lib/libncursesw.so.{self.version}")
	self.cmd_run("sed -e 's/^#if.*XOPEN.*$/#if 1/' -i dest/usr/include/curses.h")
	self.cmd_run("cp -av dest/* /")
	self.cmd_run(
		 "for lib in ncurses form panel menu ; do"
		 " ln -sfv lib${lib}w.so /usr/lib/lib${lib}.so &&"
		 " ln -sfv ${lib}w.pc /usr/lib/pkgconfig/${lib}.pc; "
		 "done"
	)
	self.cmd_run("ln -sfv libncursesw.so /usr/lib/libcurses.so")
	self.cmd_run(f"cp -v -R doc -T /usr/share/doc/ncurses-{self.version}")
	self.cmd_run("make distclean")
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		 " --with-shared"
		 " --without-normal"
		 " --without-debug"
		 " --without-cxx-binding"
		 " --with-abi-version=5"
	)
	self.cmd_run("make sources libs")
	self.cmd_run("cp -av lib/lib*.so.5* /usr/lib")
