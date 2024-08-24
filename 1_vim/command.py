#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run("echo '#define SYS_VIMRC_FILE \"/etc/vimrc\"' >> src/feature.h")
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("chown -R tester .")
	self.cmd_run("su tester -c \"TERM=xterm-256color LANG=en_US.UTF-8 make -j1 test\" >& vim-test.log")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(f"ln -fsv vim {PREFIX}/bin/vi")
	self.cmd_run(
		f"for L in {PREFIX}/share/man/""{,*/}man1/vim.1; do"
		 " ln -sfv vim.1 $(dirname $L)/vi.1;"
		 " done"
	)
	self.cmd_run(f"ln -sfv ../vim/vim91/doc {PREFIX}/share/doc/vim-{self.version}")
