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
		f" -Dprefix={PREFIX}"
		f" -Dvendorprefix={PREFIX}"
		f" -Dprivlib={PREFIX}/lib/perl5/{short_ver}/core_perl"
		f" -Darchlib={PREFIX}/lib/perl5/{short_ver}/core_perl"
		f" -Dsitelib={PREFIX}/lib/perl5/{short_ver}/site_perl"
		f" -Dsitearch={PREFIX}/lib/perl5/{short_ver}/site_perl"
		f" -Dvendorlib={PREFIX}/lib/perl5/{short_ver}/vendor_perl"
		f" -Dvendorarch={PREFIX}/lib/perl5/{short_ver}/vendor_perl"
		f" -Dman1dir={PREFIX}/share/man/man1"
		f" -Dman3dir={PREFIX}/share/man/man3"
		f" -Dpager='{PREFIX}/bin/less -isR'"
		 " -Duseshrplib"
		 " -Dusethreads"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run(f"TEST_JOBS={NB_PROC} make test_harness")

def install(self):
	self.cmd_run("make install")
