#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	download_package(self, "1_systemd-man-pages")
	download_package(self, "1_udev-lfs")
	self.chroot()
	self.cmd_run(
		 "sed -i -e 's/GROUP=\"render\"/GROUP=\"video\"/'"
		 " -e 's/GROUP=\"sgx\", //' rules.d/50-udev-default.rules.in"
	)
	self.cmd_run("sed '/systemd-sysctl/s/^/#/' -i rules.d/99-systemd.rules.in")
	self.cmd_run("sed '/NETWORK_DIRS/s/systemd/udev/' -i src/basic/path-lookup.h")
	self.take_build()
	self.cmd_run(
		 "meson setup .."
		 " --prefix=/usr"
		 " --buildtype=release"
		 " -D mode=release"
		 " -D dev-kvm-mode=0660"
		 " -D link-udev-shared=false"
		 " -D logind=false"
		 " -D vconsole=false"
	)

def compile(self):
	self.cmd_run(
		 "export udev_helpers=$(grep \"'name' :\" ../src/udev/meson.build |"
		 " awk '{print $3}' | tr -d \",'\" | grep -v 'udevadm') &&"
		 " ninja udevadm systemd-hwdb"
		 " $(ninja -n | grep -Eo '(src/(lib)?udev|rules.d|hwdb.d)/[^ ]*')"
		 " $(realpath libudev.so --relative-to .)"
		 " ${udev_helpers}"
	)

def install(self):
	self.cmd_run("install -vm755 -d {/usr/lib,/etc}/udev/{hwdb.d,rules.d,network}")
	self.cmd_run("install -vm755 -d /usr/{lib,share}/pkgconfig")
	self.cmd_run("install -vm755 udevadm /usr/bin/")
	self.cmd_run("install -vm755 systemd-hwdb /usr/bin/udev-hwdb")
	self.cmd_run("ln -svfn ../bin/udevadm /usr/sbin/udevd")
	self.cmd_run("cp -av libudev.so{,*[0-9]} /usr/lib/")
	self.cmd_run("install -vm644 ../src/libudev/libudev.h /usr/include/")
	self.cmd_run("install -vm644 src/libudev/*.pc /usr/lib/pkgconfig/")
	self.cmd_run("install -vm644 src/udev/*.pc /usr/share/pkgconfig/")
	self.cmd_run("install -vm644 ../src/udev/udev.conf /etc/udev/")
	self.cmd_run("install -vm644 rules.d/* ../rules.d/README /usr/lib/udev/rules.d/")
	self.cmd_run("install -vm644 $(find ../rules.d/*.rules -not -name '*power-switch*') /usr/lib/udev/rules.d/")
	self.cmd_run("install -vm644 hwdb.d/*  ../hwdb.d/{*.hwdb,README} /usr/lib/udev/hwdb.d/")
	self.cmd_run(
		 "export udev_helpers=$(grep \"'name' :\" ../src/udev/meson.build |"
		 " awk '{print $3}' | tr -d \",'\" | grep -v 'udevadm') &&"
		 "install -vm755 ${udev_helpers} /usr/lib/udev"
	)
	self.cmd_run("install -vm644 ../network/99-default.link /usr/lib/udev/network")
	udev_lfs = get_package_from_name("1_udev-lfs")
	self.cmd_run(f"tar -xvf /sources/{udev_lfs.file_name}")
	self.cmd_run("make -f udev-lfs-20230818/Makefile.lfs install")
	systemd_man = get_package_from_name("1_systemd-man-pages")
	self.cmd_run(
		 "tar --no-same-owner --strip-components=1"
		f" -xvf /sources/{systemd_man.file_name}"
		 " -C /usr/share/man"
		 " --wildcards '*/udev*' '*/libudev*'"
		 " '*/systemd.link.5'"
		 " '*/systemd-'{hwdb,udevd.service}.8"
	)
	self.cmd_run(
		 "sed 's|systemd/network|udev/network|'"
		 " /usr/share/man/man5/systemd.link.5 > /usr/share/man/man5/udev.link.5"
	)
	self.cmd_run(
		 "sed 's/systemd\\(\\\\\\?-\\)/udev\\1/' /usr/share/man/man8/systemd-hwdb.8"
		 " > /usr/share/man/man8/udev-hwdb.8"
	)
	self.cmd_run(
		 "sed 's|lib.*udevd|sbin/udevd|' /usr/share/man/man8/systemd-udevd.service.8"
		 " > /usr/share/man/man8/udevd.8"
	)
	self.cmd_run("rm /usr/share/man/man*/systemd*")
	self.cmd_run("udev-hwdb update")
