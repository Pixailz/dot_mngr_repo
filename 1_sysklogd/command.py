#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run("sed -i '/Error loading kernel symbols/{n;n;d}' ksym_mod.c")
	self.cmd_run("sed -i 's/union wait/int/' syslogd.c")

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make BINDIR=/sbin install")
