#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()

def compile(self):
	self.cmd_run("make prefix=/usr")

def check(self):
	self.cmd_run("make check")

def install(self):
	self.cmd_run('make prefix=/usr install && rm -fv /usr/lib/libzstd.a')
