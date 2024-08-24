#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run("sed -i 's/groups$(EXEEXT) //' src/Makefile.in")
	self.cmd_run("find man -name Makefile.in -exec sed -i 's/groups\\.1 / /'   {} \\;")
	self.cmd_run("find man -name Makefile.in -exec sed -i 's/getspnam\\.3 / /' {} \\;")
	self.cmd_run("find man -name Makefile.in -exec sed -i 's/passwd\\.5 / /'   {} \\;")
	self.cmd_run(
		 "sed -e 's:#ENCRYPT_METHOD DES:ENCRYPT_METHOD YESCRYPT:'"
		 " -e 's:/var/spool/mail:/var/mail:'"
		 " -e '/PATH=/{s@/sbin:@@;s@/bin:@@}'"
		 " -i etc/login.defs"
	)
	self.cmd_run(f"touch {PREFIX}/bin/passwd")
	self.cmd_run(
		 "./configure"
		 " --sysconfdir=/etc"
		 " --disable-static"
		 " --with-{b,yes}crypt"
		 " --without-libbsd"
		 " --with-group-name-max-length=32"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run(f"make exec_prefix={PREFIX} install")
	self.cmd_run("make -C man install-man")
	self.cmd_run("pwconv")
	self.cmd_run("grpconv")
	self.cmd_run("mkdir -p /etc/default")
	self.cmd_run("useradd -D --gid 999")
	self.cmd_run("sed -i '/MAIL/s/yes/no/' /etc/default/useradd")

