#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	download_package(self, "1_systemd-man-pages")
	self.chroot()
	self.cmd_run(
		 "sed -i -e 's/GROUP=\"render\"/GROUP=\"video\"/'"
		 " -e 's/GROUP=\"sgx\", //' rules.d/50-udev-default.rules.in"
	)
	self.take_build()
	self.cmd_run(
		 "meson setup"
		f" --prefix={PREFIX}"
		 " --buildtype=release"
		 " -D default-dnssec=no"
		 " -D firstboot=false"
		 " -D install-tests=false"
		 " -D ldconfig=false"
		 " -D sysusers=false"
		 " -D rpmmacrosdir=no"
		 " -D homed=disabled"
		 " -D userdb=false"
		 " -D man=disabled"
		 " -D mode=release"
		 " -D pamconfdir=no"
		 " -D dev-kvm-mode=0660"
		 " -D nobody-group=nogroup"
		 " -D sysupdate=disabled"
		 " -D ukify=disabled"
		f" -D docdir={PREFIX}/share/doc/systemd-{self.version}"
		 " .."
	)

def compile(self):
	self.cmd_run("ninja")

# def check(self):
# 	self.cmd_run("echo 'NAME=\"Linux From Scratch\"' > /etc/os-release")
# 	self.cmd_run("ninja test")

def install(self):
	self.cmd_run("ninja install")
	systemd_man = get_package_from_name("1_systemd-man-pages")
	self.cmd_run(
		 "tar --no-same-owner --strip-components=1"
		f" -xvf /sources/{systemd_man.file_name}"
		f" -C {PREFIX}/share/man"
	)
	self.cmd_run("systemd-machine-id-setup")
	self.cmd_run("systemctl preset-all")
