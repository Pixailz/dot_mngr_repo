#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	download_package(self, "blfs-systemd-units")
	self.chroot()
	self.cmd_run("install -v -g sys -m700 -d /var/lib/sshd")
	# TODO: Allow modification of /etc/passwd and /etc/group
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --sysconfdir=/etc/ssh"
		 " --with-privsep-path=/var/lib/sshd"
		f" --with-default-path={PREFIX}/bin"
		f" --with-superuser-path={PREFIX}/sbin:{PREFIX}/bin"
		 " --with-pid-dir=/run"
	)

def compile(self):
	self.cmd_run("make")

# def check(self):
# 	self.cmd_run("make tests", 1)

def install(self):
	self.cmd_run("make install")
	self.cmd_run(f"install -v -m755 contrib/ssh-copy-id {PREFIX}/bin")
	self.cmd_run("install -v -m644 contrib/ssh-copy-id.1 /usr/share/man/man1")
	self.cmd_run(
		 "install -v -m755 -d"
		f" {PREFIX}/share/doc/openssh-{self.version}"
	)
	self.cmd_run(
		 "install -v -m644 INSTALL LICENCE OVERVIEW README*"
		f" {PREFIX}/share/doc/openssh-{self.version}"
	)
	self.install_blfs_systemd_units("sshd")