#!/usr/bin/env python3

from dot_mngr import *

def apply_patchs(self):
	if self.version != "5.2.21":
		return
	for i in range(22, 27):
		self.apply_patch(f"bash52-0{i}", "-p0")
	self.version = "5.2.26"

def configure(self):
	self.add_path(f"{PREFIX}/tools/bin")
	self.add_env({
		"LC_ALL": "POSIX",
		"CONFIG_SITE": f"{PREFIX}/usr/share/config.site"
	})
	# apply_patchs(self)
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		 ' --build="$(sh support/config.guess)"'
		f" --host={TARGET_TRIPLET}"
		 " --without-bash-malloc"
		 " bash_cv_strtold_broken=no"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run(f"make DESTDIR={PREFIX} install")
	self.cmd_run(f"ln -svf bash {PREFIX}/bin/sh")
