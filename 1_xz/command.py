#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.add_path(f"{ROOT_PATH}/tools/bin")
	self.add_env({
		"LC_ALL": "POSIX",
		"CONFIG_SITE": f"{ROOT_PATH}{PREFIX}/share/config.site"
	})
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		f" --host={TARGET_TRIPLET}"
		 " --build=$(build-aux/config.guess)"
		 " --disable-static"
		f" --docdir={PREFIX}/share/doc/xz-{self.version}"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run(f"make DESTDIR={ROOT_PATH} install")
	self.cmd_run(f"rm -f {ROOT_PATH}{PREFIX}/lib/liblzma.la")
