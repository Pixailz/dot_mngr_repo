#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.add_path(f"{ROOT_PATH}/tools/bin")
	self.add_env({
		"LC_ALL": "POSIX",
		"CONFIG_SITE": f"{ROOT_PATH}{PREFIX}/share/config.site"
	})
	self.cmd_run("sed '6009s/$add_dir//' -i ltmain.sh")
	self.take_build()
	self.cmd_run(
		 "../configure"
		f" --prefix={PREFIX}"
		 " --build=$(../config.guess)"
		f" --host={TARGET_TRIPLET}"
		 " --disable-nls"
		 " --enable-shared"
		 " --enable-gprofng=no"
		 " --disable-werror"
		 " --enable-64-bit-bfd"
		 " --enable-new-dtags"
		 " --enable-default-hash-style=gnu"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run(f"make DESTDIR={ROOT_PATH} install")
	self.cmd_run(
		f"rm -rf {ROOT_PATH}{PREFIX}"
		"/lib/lib{bfd,ctf,ctf-nobfd,opcodes,sframe}.{a,la}"
	)
