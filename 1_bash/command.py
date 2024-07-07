#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.add_path(f"{PREFIX}/tools/bin")
	self.add_env({
		"LC_ALL": "POSIX",
		"CONFIG_SITE": f"{PREFIX}/usr/share/config.site"
	})
	self.cmd_run(
		 "./configure --prefix=/usr"
		 ' --build="$(sh support/config.guess)"'
		f" --host={TARGET_TRIPLET}"
		 " --without-bash-malloc"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run(f"make DESTDIR={PREFIX} install")
	if not os.path.exists(os.path.join(PREFIX, "bin/sh")):
		self.cmd_run(f"ln -sf bash {PREFIX}/bin/sh")