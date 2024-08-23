#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	# self.cmd_run("echo '#define PATH_PROCNET_DEV \"/proc/net/dev\"' >> ifconfig/system/linux.h")
	self.cmd_run("sed -i 's/def HAVE_TERMCAP_TGETENT/ 1/' telnet/telnet.c")
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		 " --bindir=/usr/bin"
		 " --localstatedir=/var"
		 " --disable-logger"
		 " --disable-whois"
		 " --disable-rcp"
		 " --disable-rexec"
		 " --disable-rlogin"
		 " --disable-rsh"
		 " --disable-servers"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
	self.cmd_run("mv -v /usr/{,s}bin/ifconfig")
