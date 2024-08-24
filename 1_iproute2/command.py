#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run("sed -i /ARPD/d Makefile")
	self.cmd_run("rm -fv man/man8/arpd.8")

def compile(self):
	self.cmd_run("make NETNS_RUN_DIR=/run/netns")

def install(self):
	self.cmd_run(f"make SBINDIR={PREFIX}/sbin install")
	self.cmd_run(f"mkdir -pv {PREFIX}/share/doc/iproute2-{self.version}")
	self.cmd_run(f"cp -v COPYING README* {PREFIX}/share/doc/iproute2-{self.version}")
