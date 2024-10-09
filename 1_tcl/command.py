#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	download_package(self, "1_tcl-doc")
	self.chroot()
	path = self.chrooted_get_path(self.archive_folder, self.chrooted)
	Os.take(os.path.join(path, "unix"))
	self.cmd_run(
		f"./configure"
		f" --prefix={PREFIX}"
		f" --mandir={PREFIX}/share/man"
		 " --disable-rpath"
	)

def compile(self):
	self.cmd_run("make")
	path = self.chrooted_get_path(self.archive_folder, self.chrooted)
	self.cmd_run(
		f"sed -e 's|{path}/unix|{PREFIX}/lib|'"
		f" -e 's|{path}|{PREFIX}/include|'"
		 " -i tclConfig.sh"
	)
	self.cmd_run(
		f"sed -e 's|{path}/unix/pkgs/tdbc1.1.7|{PREFIX}/lib/tdbc1.1.7|'"
		f" -e 's|{path}/pkgs/tdbc1.1.7/generic|{PREFIX}/include|'"
		f" -e 's|{path}/pkgs/tdbc1.1.7/library|{PREFIX}/lib/tcl8.6|'"
		f" -e 's|{path}/pkgs/tdbc1.1.7|{PREFIX}/include|'"
		 " -i pkgs/tdbc1.1.7/tdbcConfig.sh"
	)
	self.cmd_run(
		f"sed -e 's|{path}/unix/pkgs/itcl4.2.4|{PREFIX}/lib/itcl4.2.4|'"
		f" -e 's|{path}/pkgs/itcl4.2.4/generic|{PREFIX}/include|'"
		f" -e 's|{path}/pkgs/itcl4.2.4|{PREFIX}/include|'"
		 " -i pkgs/itcl4.2.4/itclConfig.sh"
	)

def check(self):
	self.cmd_run("make test")

def install(self):
	path = self.chrooted_get_path(self.archive_folder, self.chrooted)
	self.cmd_run("make install")
	self.cmd_run(f"chmod -v u+w {PREFIX}/lib/libtcl8.6.so")
	self.cmd_run("make install-private-headers")
	self.cmd_run(f"ln -sfv tclsh8.6 {PREFIX}/bin/tclsh")
	self.cmd_run(f"mv {PREFIX}/share/man/man3/" "{Thread,Tcl_Thread}.3")
	Os.take(path)
	extract_file_from_package("1_tcl-doc", self.archive_folder, self.chrooted)
	self.cmd_run(f"mkdir -v -p {PREFIX}/share/doc/tcl-{self.version}")
