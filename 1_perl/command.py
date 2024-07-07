#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	short_ver = self.version.split(".")
	short_ver = ".".join(short_ver[:-1])

	self.cmd_run(
		 "sh Configure -des"
		f" -Dprefix=/usr"
		 " -Dvendorprefix=/usr"
		 " -Duseshrplib"
		f" -Dprivlib=/usr/lib/perl5/{short_ver}/core_perl"
		f" -Darchlib=/usr/lib/perl5/{short_ver}/core_perl"
		f" -Dsitelib=/usr/lib/perl5/{short_ver}/site_perl"
		f" -Dsitearch=/usr/lib/perl5/{short_ver}/site_perl"
		f" -Dvendorlib=/usr/lib/perl5/{short_ver}/vendor_perl"
		f" -Dvendorarch=/usr/lib/perl5/{short_ver}/vendor_perl"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install")
