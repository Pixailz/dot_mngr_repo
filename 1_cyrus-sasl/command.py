#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run("sed '/saslint/a #include <time.h>' -i lib/saslutil.c")
	self.cmd_run("sed '/plugin_common/a #include <time.h>' -i plugins/cram.c")
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --sysconfdir=/etc"
         " --enable-auth-sasldb"
         " --with-dblib=lmdb"
         " --with-dbpath=/var/lib/sasl/sasldb2"
         " --with-sphinx-build=no"
         " --with-saslauthd=/var/run/saslauthd"
	)

def compile(self):
	self.cmd_run("make", 1)

def install(self):
	self.cmd_run("make install")
	path = f"{PREFIX}/share/doc/cyrus-sasl-{self.version}"
	self.cmd_run(f"install -v -dm755 {path}/html")
	self.cmd_run(f"install -v -m644 saslauthd/LDAP_SASLAUTHD {path}")
	self.cmd_run(f"install -v -m644 doc/legacy/*.html {path}/html")
	self.cmd_run("install -v -dm700 /var/lib/sasl")
