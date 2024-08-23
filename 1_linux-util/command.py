#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run("mkdir -pv /var/lib/hwclock")
	self.cmd_run(
		"./configure"
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
		" --disable-liblastlog2"
        " --without-python"
        " ADJTIME_PATH=/var/lib/hwclock/adjtime"
       f" --docdir=/usr/share/doc/util-linux-{self.version}"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install")
