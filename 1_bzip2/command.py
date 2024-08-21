#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.apply_patch("bzip2-1.0.8-install_docs-1", "-Np1")
	self.chroot()
	self.cmd_run(
		"sed -i 's@\\(ln -s -f \\)\\$(PREFIX)/bin/@\\1@' Makefile && "
		"sed -i 's@(PREFIX)/man@(PREFIX)/share/man@g' Makefile && "
		"make -f Makefile-libbz2_so && make clean"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run(
		 "make PREFIX=/usr install && "
		 "cp -av libbz2.so.* /usr/lib && "
		f"ln -fsv libbz2.so.{self.version} /usr/lib/libbz2.so && "
	 	 "cp -v bzip2-shared /usr/bin/bzip2 && "
		 "for i in /usr/bin/{bzcat,bunzip2}; do ln -sfv bzip2 $i; done && "
		 "rm -fv /usr/lib/libbz2.a"
	)
