#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	download_package(self, "1_tcl-doc")
	self.chroot()
	path = self.chrooted_get_path(self.tar_folder, self.chrooted)
	Os.take(os.path.join(path, "unix"))
	self.cmd_run(
		f"./configure"
		 " --prefix=/usr"
		 " --mandir=/usr/share/man"
		 " --disable-rpath"
	)

def compile(self):
	self.cmd_run("make")
	path = self.chrooted_get_path(self.tar_folder, self.chrooted)
	self.cmd_run(
		f"sed -e 's|{path}/unix|/usr/lib|'"
		f" -e 's|{path}|/usr/include|'"
		 " -i tclConfig.sh"
	)
	self.cmd_run(
		f"sed -e 's|{path}/unix/pkgs/tdbc1.1.7|/usr/lib/tdbc1.1.7|'"
		f" -e 's|{path}/pkgs/tdbc1.1.7/generic|/usr/include|'"
		f" -e 's|{path}/pkgs/tdbc1.1.7/library|/usr/lib/tcl8.6|'"
		f" -e 's|{path}/pkgs/tdbc1.1.7|/usr/include|'"
		 " -i pkgs/tdbc1.1.7/tdbcConfig.sh"
	)
	self.cmd_run(
		f"sed -e 's|{path}/unix/pkgs/itcl4.2.4|/usr/lib/itcl4.2.4|'"
		f" -e 's|{path}/pkgs/itcl4.2.4/generic|/usr/include|'"
		f" -e 's|{path}/pkgs/itcl4.2.4|/usr/include|'"
		 " -i pkgs/itcl4.2.4/itclConfig.sh"
	)

def check(self):
	self.cmd_run("make test")

def install(self):
	path = self.chrooted_get_path(self.tar_folder, self.chrooted)
	self.cmd_run("make install")
	self.cmd_run("chmod -v u+w /usr/lib/libtcl8.6.so")
	self.cmd_run("make install-private-headers")
	self.cmd_run("ln -sfv tclsh8.6 /usr/bin/tclsh")
	self.cmd_run("mv /usr/share/man/man3/{Thread,Tcl_Thread}.3")
	Os.take(path)
	extract_file_from_package("1_tcl-doc", self.tar_folder, self.chrooted)
	self.cmd_run(f"mkdir -v -p /usr/share/doc/tcl-{self.version}")
