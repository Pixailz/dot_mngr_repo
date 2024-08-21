#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run("sed -i '/\"lib64\"/s/64//' Modules/GNUInstallDirs.cmake ")
	self.cmd_run(
		 "./bootstrap"
		 " --prefix=/usr"
		 " --system-libs"
		 " --mandir=/share/man"
		 " --no-system-jsoncpp"
		 " --no-system-cppdap"
		 " --no-system-librhash"
		f" --docdir=/share/doc/cmake-{self.version}"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run(
		f"LC_ALL=en._US.UTF-8 bin/ctest -j{NB_CORE}"
		f" -O cmake-{self.version}-test.log"
	)

def install(self):
	self.cmd_run("make install")
