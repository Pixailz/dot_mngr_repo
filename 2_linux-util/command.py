#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()

	if os.getenv("LFS_SYSTEMD"):
		SYSTEMD_FLAG = ""
	else:
		SYSTEMD_FLAG = "--without-systemd{,systemunitdir}"

	self.cmd_run(
		"./configure"
		" --bindir=/usr/bin"
		" --libdir=/usr/lib"
		" --runstatedir=/run"
		" --sbindir=/usr/sbin"
        " --disable-chfn-chsh"
        " --disable-login"
        " --disable-nologin"
        " --disable-su"
        " --disable-setpriv"
        " --disable-runuser"
        " --disable-pylibmount"
        " --disable-liblastlog2"
        " --disable-static"
        " --without-python" +
		SYSTEMD_FLAG +
        " ADJTIME_PATH=/var/lib/hwclock/adjtime"
       f" --docdir=/usr/share/doc/util-linux-{self.version}"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("touch /etc/fstab")
	self.cmd_run("chown -R tester .")
	self.cmd_run('su tester -c "make -k check"')

def install(self):
	self.cmd_run("make install")
