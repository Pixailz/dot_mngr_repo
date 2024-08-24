#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()

def compile(self):
	self.cmd_run(
		 "pip3 wheel"
		 " -w dist"
		 " --no-cache-dir"
		 " --no-build-isolation"
		 " --no-deps"
		 " ${PWD}"
	)

def install(self):
	self.cmd_run(
		 "pip3 install"
		 " --no-index"
		 " --find-links dist"
		 " meson"
	)
	self.cmd_run(f"install -vDm644 data/shell-completions/bash/meson {PREFIX}/share/bash-completion/completions/meson")
	self.cmd_run(f"install -vDm644 data/shell-completions/zsh/_meson {PREFIX}/share/zsh/site-functions/_meson")
