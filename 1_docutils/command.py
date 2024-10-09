#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		f"for f in {PREFIX}/bin/rst*.py; do"
		 "    echo $f; "
		f"    rm -fv {PREFIX}/bin/$(basename $f .py); "
		 "done"
	)
	self.cmd_run(
		f"find {PREFIX}/lib/python3.12/site-packages/ -name 'docutils*'"
		 " -exec rm -rf {} \; || true"
	)

def compile(self):
	self.cmd_run(
		 "pip3 wheel"
		 " -w dist"
		 " --no-build-isolation"
		 " --no-deps"
		 " --no-cache-dir"
		 " $PWD"
	)

def install(self):
	self.cmd_run(
		 "pip3 install"
		 " --no-index"
		 " --find-links=dist"
		 " --no-cache-dir"
		 " --no-user"
		 " docutils"
	)