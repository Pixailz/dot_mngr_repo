#!/usr/bin/env python3

from dot_mngr import *

def download_patchs(self):
	if self.version != "5.2.21":
		return
	for i in range(22, 27):
		self.download_patch(f"bash52-0{i}")
		print(f"bash52-0{i}")
	self.version = "5.2.26"

def apply_patchs(self):
	if self.version != "5.2.21":
		return
	for i in range(22, 27):
		self.apply_patch(f"bash52-0{i}", "-p0")
	self.version = "5.2.26"

def configure(self):
	download_patchs(self)
	self.chroot()
	# apply_patchs(self)
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --without-bash-malloc"
		 " --with-installed-readline"
		 " bash_cv_strtold_broken=no"
		f" --docdir={PREFIX}/share/doc/bash-{self.version}"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run(
		"cat > /tmp/e <<EOF\n"
		"set timeout -1\n"
		"spawn make tests\n"
		"expect eof\n"
		"lassign [wait] _ _ _ value\n"
		"exit ${value}\n"
		"EOF"
	)
	self.cmd_run("chown -R tester .")
	self.cmd_run(f"su -s {PREFIX}/bin/expect tester </tmp/e")
	self.cmd_run("rm -rf /tmp/e")

def install(self):
	self.cmd_run(f"make install")
