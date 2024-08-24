#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()

	SYSTEMD_FLAG = " --with-systemd" if os.getenv("LFS_SYSTEMD") else ""

	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		f" --docdir={PREFIX}/share/doc/procps-ng-{self.version}"
		 " --disable-static"
		 " --disable-kill" +
		 SYSTEMD_FLAG
	)

def compile(self):
	if os.getenv("LFS_SYSTEMD"):
		self.cmd_run("make src_w_LDADD='$(LDADD) -lsystemd'")
	else:
		self.cmd_run("make")

def check(self):
	self.cmd_run("chown -R tester .")
	self.cmd_run('su tester -c "PATH=$PATH make check"')

def install(self):
	self.cmd_run("make install")
