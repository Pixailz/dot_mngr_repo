#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run("sed -i '/install -m.*STA/d' libcap/Makefile")

def compile(self):
	self.cmd_run("make prefix=/usr lib=lib")

def check(self):
	self.cmd_run("make test")

def install(self):
	self.cmd_run("make prefix=/usr lib=lib install")
