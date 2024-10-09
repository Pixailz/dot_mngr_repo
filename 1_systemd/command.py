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
	homed = "homed=disabled"
	if	conf.is_installed("1_cryptsetup", False) and \
		conf.is_installed("1_libpwquality", False):
		homed = "homed=enabled"
	self.cmd_run(
		 "meson setup"
		f" --prefix={PREFIX}"
		 " --buildtype=release"
		 " -D default-dnssec=no"
		 " -D firstboot=false"
		 " -D install-tests=false"
		 " -D ldconfig=false"
    	 " -D man=auto"
		 " -D sysusers=false"
		 " -D rpmmacrosdir=no"
		f" -D {homed}"
		 " -D userdb=false"
		 " -D mode=release"
		 " -D pam=enabled"
		 " -D pamconfdir=/etc/pam.d"
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
	systemd_man = conf.get_package("1_systemd-man-pages")
	systemd_man.prepare_archive(chroot = self.chrooted)
	self.cmd_run(
		 "tar --no-same-owner --strip-components=1"
		f" -xvf {self.chrooted_get_path(systemd_units.archive_folder, self.chrooted)}"
		f" -C {PREFIX}/share/man"
	)
	self.cmd_run("systemd-machine-id-setup")
	self.cmd_run("systemctl preset-all")
