#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run("sed -i '/cmptest/d' tests/CMakeLists.txt")
	self.take_build()
	self.cmd_run(
		 "cmake .."
		f" -D CMAKE_INSTALL_PREFIX={PREFIX}"
	)

def compile(self):
	self.cmd_run("make")

# def check(self):
# 	self.cmd_run("make test")

def install(self):
	self.cmd_run("make docs")
	self.cmd_run("make install")
	self.cmd_run(
		 "install -v -d -m755"
		f" {PREFIX}/share/doc/graphite2-{self.version}"
	)
	# self.cmd_run(
	# 	 "cp -v -f doc/{GTF,manual}.html"
	# 	f" {PREFIX}/share/doc/graphite2-{self.version}"
	# )
	# self.cmd_run(
	# 	 "cp -v -f doc/{GTF,manual}.pdf"
	# 	f" {PREFIX}/share/doc/graphite2-{self.version}"
	# )
