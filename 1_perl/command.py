#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.add_env({
		"LC_ALL": "POSIX",
	})
	short_ver = self.version.split(".")
	short_ver = ".".join(short_ver[:-1])

	self.cmd_run(
		 "sh Configure -des"
		f" -D prefix=/usr"
		 " -D vendorprefix=/usr"
		 " -D useshrplib"
		f" -D privlib=/usr/lib/perl5/{short_ver}/core_perl"
		f" -D archlib=/usr/lib/perl5/{short_ver}/core_perl"
		f" -D sitelib=/usr/lib/perl5/{short_ver}/site_perl"
		f" -D sitearch=/usr/lib/perl5/{short_ver}/site_perl"
		f" -D vendorlib=/usr/lib/perl5/{short_ver}/vendor_perl"
		f" -D vendorarch=/usr/lib/perl5/{short_ver}/vendor_perl"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install")
