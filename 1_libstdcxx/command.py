#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.add_path(f"{PREFIX}/tools/bin")
	self.add_env({
		"LC_ALL": "POSIX",
		"CONFIG_SITE": f"{PREFIX}/usr/share/config.site"
	})
	self.take_build()
	self.cmd_run(
		 "../libstdc++-v3/configure"
		f" --host={TARGET_TRIPLET}"
		 " --build=$(../config.guess)"
		 " --prefix=/usr"
		 " --disable-multilib"
		 " --disable-nls"
		 " --disable-libstdcxx-pch"
		f" --with-gxx-include-dir=/tools/{TARGET_TRIPLET}/include/c++/{self.version}"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run(
		f'make DESTDIR="{PREFIX}" install &&'
		f' rm -rf "{PREFIX}/usr/lib/lib"'
		 "{stdc++{,exp,fs},supc++}.la"
	)
