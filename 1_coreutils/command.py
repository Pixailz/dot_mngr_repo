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
		f" --host={TARGET_TRIPLET}"
		 ' --build="$(build-aux/config.guess)"'
		 " --enable-install-program=hostname"
		 " --enable-no-install-program=kill,uptime"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run(f'make DESTDIR="{PREFIX}" install')
	self.cmd_run(f"mv -f {PREFIX}/usr/bin/chroot {PREFIX}/usr/sbin/chroot")
	self.cmd_run(f"mkdir -p {PREFIX}/usr/share/man/man8")
	self.cmd_run(f"mv -f {PREFIX}/usr/share/man/man1/chroot.1 {PREFIX}/usr/share/man/man8/chroot.8")
	self.cmd_run(f"sed -i 's/\"1\"/\"8\"/' {PREFIX}/usr/share/man/man8/chroot.8")
