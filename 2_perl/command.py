#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	short_ver = self.version.split(".")
	short_ver = ".".join(short_ver[:-1])

	self.cmd_run(
		 "export BUILD_ZLIB=False &&"
		 " export BUILD_BZIP2=0 &&"
		 " sh Configure -des"
		 " -Dprefix=/usr"
		 " -Dvendorprefix=/usr"
		f" -Dprivlib=/usr/lib/perl5/{short_ver}/core_perl"
		f" -Darchlib=/usr/lib/perl5/{short_ver}/core_perl"
		f" -Dsitelib=/usr/lib/perl5/{short_ver}/site_perl"
		f" -Dsitearch=/usr/lib/perl5/{short_ver}/site_perl"
		f" -Dvendorlib=/usr/lib/perl5/{short_ver}/vendor_perl"
		f" -Dvendorarch=/usr/lib/perl5/{short_ver}/vendor_perl"
		 " -Dman1dir=/usr/share/man/man1"
		 " -Dman3dir=/usr/share/man/man3"
		 " -Dpager='/usr/bin/less -isR'"
		 " -Duseshrplib"
		 " -Dusethreads"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run(f"TEST_JOBS={NB_PROC} make test_harness")

def install(self):
	self.cmd_run("make install")
