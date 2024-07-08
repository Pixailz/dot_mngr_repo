#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	download_package(self, "1_systemd-man-pages")
	self.download_patch("systemd-255-upstream_fixes-1")
	self.chroot()
	self.cmd_run(
		 "sed -i -e 's/GROUP=\"render\"/GROUP=\"video\"/'"
		 " -e 's/GROUP=\"sgx\", //' rules.d/50-udev-default.rules.in"
	)
	self.apply_patch("systemd-255-upstream_fixes-1", "-Np1")
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
	)
	self.take_build()
	self.cmd_run(
		 "meson setup"
		 " --prefix=/usr"
		 " --buildtype=release"
		 " -Ddefault-dnssec=no"
		 " -Dfirstboot=false"
		 " -Dinstall-tests=false"
		 " -Dldconfig=false"
		 " -Dsysusers=false"
		 " -Drpmmacrosdir=no"
		 " -Dhomed=disabled"
		 " -Duserdb=false"
		 " -Dman=disabled"
		 " -Dmode=release"
		 " -Dpamconfdir=no"
		 " -Ddev-kvm-mode=0660"
		 " -Dnobody-group=nogroup"
		 " -Dsysupdate=disabled"
		 " -Dukify=disabled"
		f" -Ddocdir=/usr/share/doc/systemd-{self.version}"
		 " .."
	)

def compile(self):
	self.cmd_run("ninja")

def install(self):
	self.cmd_run("ninja install")
	systemd_man = get_package_from_name("1_systemd-man-pages")
	self.cmd_run(
		 "tar --no-same-owner --strip-components=1"
		f" -xvf /sources/{systemd_man.file_name}"
		 " -C /usr/share/man"
	)
	self.cmd_run("systemd-machine-id-setup")
	self.cmd_run("systemctl preset-all")
