#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	short_ver = self.version.split(".")
	short_ver = ".".join(short_ver[:-1])

	self.cmd_run(
		 "sh Configure -des"
		f" -D prefix={PREFIX}"
		f" -D vendorprefix={PREFIX}"
		 " -D useshrplib"
		f" -D privlib={PREFIX}/lib/perl5/{short_ver}/core_perl"
		f" -D archlib={PREFIX}/lib/perl5/{short_ver}/core_perl"
		f" -D sitelib={PREFIX}/lib/perl5/{short_ver}/site_perl"
		f" -D sitearch={PREFIX}/lib/perl5/{short_ver}/site_perl"
		f" -D vendorlib={PREFIX}/lib/perl5/{short_ver}/vendor_perl"
		f" -D vendorarch={PREFIX}/lib/perl5/{short_ver}/vendor_perl"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install")
