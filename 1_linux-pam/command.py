#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	download_package(self, "1_linux-pam_doc")
	self.chroot()
	linux_pam_doc = conf.get_package("1_linux-pam_doc")
	self.cmd_run(
		 "tar --no-same-owner --strip-components=1"
		f" -xvf /sources/{linux_pam_doc.file_name}"
	)
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
        f" --sbindir={PREFIX}/sbin"
         " --sysconfdir=/etc"
        f" --libdir={PREFIX}/lib"
        f" --enable-securedir={PREFIX}/lib/security"
		f" --docdir={PREFIX}/share/doc/Linux-PAM-{self.version}"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("install -v -m755 -d /etc/pam.d")
	self.cmd_run(
		 "cat > /etc/pam.d/other << \"EOF\"\n"
		 "auth     required       pam_deny.so\n"
		 "account  required       pam_deny.so\n"
		 "password required       pam_deny.so\n"
		 "session  required       pam_deny.so\n"
		 "EOF"
	)
	self.cmd_run("make check")
	self.cmd_run("rm -fv /etc/pam.d/other")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(f"chmod -v 4755 {PREFIX}/sbin/unix_chkpwd")
