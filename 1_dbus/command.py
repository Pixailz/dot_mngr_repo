#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		 " --sysconfdir=/etc"
         " --localstatedir=/var"
         " --runstatedir=/run"
         " --enable-user-session"
         " --disable-static"
         " --disable-doxygen-docs"
         " --disable-xml-docs"
        f" --docdir=/usr/share/doc/dbus-{self.version}"
         " --with-system-socket=/run/dbus/system_bus_socket"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
	self.cmd_run("ln -sfv /etc/machine-id /var/lib/dbus")
