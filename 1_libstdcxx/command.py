#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.take_build()
	self.cmd_run(
		 "../libstdc++-v3/configure"
		f" --host={TARGET_TRIPLET}"
		 " --build=$(../config.guess)"
		f" --prefix=/usr"
		 " --disable-multilib"
		 " --disable-nls"
		 " --disable-libstdcxx-pch"
		f" --with-gxx-include-dir=/tools/{TARGET_TRIPLET}/include/c++/{self.version}"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	pass

def install(self):
	self.cmd_run(
		f'make DESTDIR="{PREFIX}" install &&'
		f' rm -rf "{PREFIX}/usr/lib/lib"'
		 "{stdc++{,exp,fs},supc++}.la"
	)

def uninstall(self):
	pass
