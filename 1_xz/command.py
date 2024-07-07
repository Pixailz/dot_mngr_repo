#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.add_path(f"{PREFIX}/tools/bin")
	self.add_env({
		"LC_ALL": "POSIX",
		"CONFIG_SITE": f"{PREFIX}/usr/share/config.site"
	})
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		f' --host="{TARGET_TRIPLET}"'
		 ' --build="$(build-aux/config.guess)"'
		 " --disable-static"
		f" --docdir=/usr/share/doc/xz-{self.version}"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run(f'make DESTDIR="{PREFIX}" install')
	self.cmd_run(f"rm -f {PREFIX}/usr/lib/liblzma.la")
