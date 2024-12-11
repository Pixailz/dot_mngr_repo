#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run("mv tests/dbusmock{,-tests}")
	self.cmd_run(
		 "sed -e '/accounts_service\\.py/s/dbusmock/dbusmock-tests/'"
		 " -e 's/assertEquals/assertEqual/'"
		 " -i tests/test-libaccountsservice.py"
	)
	self.cmd_run(
		 "sed -i '/^SIMULATED_SYSTEM_LOCALE/s/en_IE.UTF-8/en_HK.iso88591/'"
		 " tests/test-daemon.py"
	)
	self.take_build()
	self.cmd_run(
		 "meson setup .."
		f" --prefix={PREFIX}"
		 " --buildtype=release"
		 " -D admin_group=adm"
	)
	self.cmd_run(
		 "grep 'print_indent' ../subprojects/mocklibc-1.0/src/netgroup.c"
		 " | sed 's/ {/;/' >> ../subprojects/mocklibc-1.0/src/netgroup.h"
    )
	self.cmd_run(
		 "sed -i '1i#include <stdio.h>'"
		 " ../subprojects/mocklibc-1.0/src/netgroup.h"
	)

def compile(self):
	self.cmd_run("ninja")

def check(self):
	self.cmd_run("ninja test")

def install(self):
	self.cmd_run("ninja install")