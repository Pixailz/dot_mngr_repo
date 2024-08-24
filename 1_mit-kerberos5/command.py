#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	Os.take("src")
	self.cmd_run("sed -i -e '/eq 0/{N;s/12 //}' plugins/kdb/db2/libdb2/test/run.test")
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --sysconfdir=/etc"
		 " --localstatedir=/var/lib"
		 " --runstatedir=/run"
		 " --with-system-et"
		 " --with-system-ss"
		 " --with-system-verto=no"
		 " --enable-dns-for-realm"
		 " --disable-rpath"
	)

def compile(self):
	self.cmd_run("make")

# def check(self):
# 	self.cmd_run("make check", 1)

def install(self):
	self.cmd_run("make install")
	self.cmd_run(f"cp -vfr ../doc -T {PREFIX}/share/doc/krb5-{self.version}")