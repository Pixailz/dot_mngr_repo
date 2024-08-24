#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.add_path(f"{ROOT_PATH}/tools/bin")
	self.add_env({
		"LC_ALL": "POSIX",
		"CONFIG_SITE": f"{ROOT_PATH}{PREFIX}/share/config.site"
	})
	self.cmd_run("make mrproper")

def compile(self):
	self.cmd_run("make headers")

def install(self):
	self.cmd_run(
		 "find usr/include -type f ! -name '*.h' -delete &&"
		f" cp -r usr/include {ROOT_PATH}{PREFIX}"
	)
