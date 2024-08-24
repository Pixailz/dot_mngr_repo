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
		 " --enable-install-program=hostname"
		 " --enable-no-install-program=kill,uptime"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run(f"make DESTDIR={ROOT_PATH} install")
	self.cmd_run(f"mv -f {ROOT_PATH}{PREFIX}/bin/chroot {ROOT_PATH}{PREFIX}/sbin/chroot")
	self.cmd_run(f"mkdir -p {ROOT_PATH}{PREFIX}/share/man/man8")
	self.cmd_run(f"mv -f {ROOT_PATH}{PREFIX}/share/man/man1/chroot.1 {ROOT_PATH}{PREFIX}/share/man/man8/chroot.8")
	self.cmd_run(f"sed -i 's/\"1\"/\"8\"/' {ROOT_PATH}{PREFIX}/share/man/man8/chroot.8")
