#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run("echo depends bli part_gpt > grub-core/extra_deps.lst")
	self.cmd_run(
		 "unset {C,CPP,CXX,LD}FLAGS && "
		 " ./configure"
		 " --prefix=/usr"
		 " --sysconfdir=/etc"
		 " --disable-efiemu"
		 " --disable-werror"
	)

def compile(self):
	self.cmd_run("unset {C,CPP,CXX,LD}FLAGS && make")

def install(self):
	self.cmd_run("unset {C,CPP,CXX,LD}FLAGS && make install")
	self.cmd_run("mv -v /etc/bash_completion.d/grub /usr/share/bash-completion/completions")
