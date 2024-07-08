#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run("sed -i '/test_mkfds/s/^/#/' tests/helpers/Makemodule.am")
	self.cmd_run(
		"./configure"
		" --bindir=/usr/bin"
		" --libdir=/usr/lib"
		" --runstatedir=/run"
        " --disable-chfn-chsh"
        " --disable-login"
        " --disable-nologin"
        " --disable-su"
        " --disable-setpriv"
        " --disable-runuser"
        " --disable-pylibmount"
        " --disable-static"
        " --without-python"
        " --without-systemd"
        " --without-systemdsystemunitdir"
        " ADJTIME_PATH=/var/lib/hwclock/adjtime"
       f" --docdir=/usr/share/doc/util-linux-{self.version}"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("chown -R tester .")
	self.cmd_run('su tester -c "make -k check"')

def install(self):
	self.cmd_run("make install")
