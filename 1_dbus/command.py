#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --sysconfdir=/etc"
		 " --localstatedir=/var"
		 " --runstatedir=/run"
		 " --enable-user-session"
		 " --disable-static"
		 " --disable-doxygen-docs"
		 " --disable-xml-docs"
		f" --docdir={PREFIX}/share/doc/dbus-{self.version}"
		 " --with-system-socket=/run/dbus/system_bus_socket"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(
		 "chown -v root:messagebus"
		f" {PREFIX}/libexec/dbus-daemon-launch-helper"
	)
	self.cmd_run(f"chmod 4750 {PREFIX}/libexec/dbus-daemon-launch-helper")

	self.cmd_run(
		 'cat << "EOF" > /etc/dbus-1/session-local.conf\n'
		 "<!DOCTYPE busconfig PUBLIC\n"
		 ' "-//freedesktop//DTD D-BUS Bus Configuration 1.0//EN"\n'
		 ' "http://www.freedesktop.org/standards/dbus/1.0/busconfig.dtd">\n'
		 '<busconfig>\n'
		 "\n"
		f"<!-- Search for .service files in {PREFIX}/local -->'\n"
		f"<servicedir>{PREFIX}/local/share/dbus-1/services</servicedir>\n"
		 "\n"
		 "</busconfig>\n"
		 "EOF"
	)