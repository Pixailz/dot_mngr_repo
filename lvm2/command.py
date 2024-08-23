#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "PATH+=:/usr/sbin"
		 " ./configure"
		 " --prefix=/usr"
		 " --enable-cmdlib"
		 " --enable-pkgconfig"
		 " --enable-udev_sync"
		 " --with-thin-check="
     	 " --with-thin-dump="
     	 " --with-thin-repair="
     	 " --with-thin-restore="
     	 " --with-cache-check="
     	 " --with-cache-dump="
     	 " --with-cache-repair="
     	 " --with-cache-restore="
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make -C tools install_tools_dynamic")
	self.cmd_run("make -C udev install")
	self.cmd_run("make -C libdm install")
	self.cmd_run("LC_ALL=en_US.UTF-8 make check_local")

def install(self):
	self.cmd_run("make install")
	self.cmd_run("make install_systemd_units")
	self.cmd_run(
		 "sed -e '/locking_dir =/{s/#//;s/var/run/}'"
		 " -i /etc/lvm/lvm.conf"
	)
