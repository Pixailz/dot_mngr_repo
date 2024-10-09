#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.download_patch("secfix-1")
	self.chroot()
	self.apply_patch("secfix-1", "-Np1")
	self.cmd_run(
		 "sed -E '/^DOCKER_TEST/,/^SSHD_TEST/s/test_(auth_keyboard_info.*"
		 " |hostkey |simple)/$(NOTHING)/' -i tests/Makefile.inc"
	)
	self.cmd_run("autoreconf -fi")
	self.cmd_run("sed 's/ssh-dss,//' -i tests/openssh_server/sshd_config")
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --disable-docker-tests"
		 " --disable-static"
	)

def compile(self):
	self.cmd_run("make")

# def check(self):
# 	self.cmd_run("make check")

def install(self):
	self.cmd_run("make install")
