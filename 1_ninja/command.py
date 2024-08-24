#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "sed -i '/int Guess/a"
		 "int   j = 0;"
		 "char* jobs = getenv( \"NINJAJOBS\" );"
		 "if ( jobs != NULL ) j = atoi( jobs );"
		 "if ( j > 0 ) return j;' src/ninja.cc"
	)

def compile(self):
	self.cmd_run(
		f"export NINJAJOBS={NB_PROC} &&"
		 " python3 configure.py --bootstrap"
	)

def install(self):
	self.cmd_run(f"install -vm755 ninja {PREFIX}/bin/")
	self.cmd_run(f"install -vDm644 misc/bash-completion {PREFIX}/share/bash-completion/completions/ninja")
	self.cmd_run(f"install -vDm644 misc/zsh-completion  {PREFIX}/share/zsh/site-functions/_ninja")
