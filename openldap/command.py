#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.download_patch("blfs-consolidate-1")
	self.chroot()
	self.apply_patch("blfs-consolidate-1", "-Np1")
	self.cmd_run("autoconf")
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		 " --sysconfdir=/etc"
		 " --localstatedir=/var"
		 " --libexecdir=/usr/lib"
         " --disable-static"
         " --disable-debug"
         " --with-tls=openssl"
         " --with-cyrus-sasl"
         " --without-systemd"
         " --enable-dynamic"
         " --enable-crypt"
         " --enable-spasswd"
         " --enable-slapd"
         " --enable-modules"
         " --enable-rlookups"
         " --enable-backends=mod"
         " --disable-sql"
         " --disable-wt"
		 " --enable-overlays=mod"
	)

def compile(self):
	self.cmd_run("make depend")
	self.cmd_run("make")

def check(self):
	self.cmd_run("make test")

def install(self):
	self.cmd_run("make install")
	self.cmd_run('sed -e "s/\\.la/.so/" -i /etc/openldap/slapd.{conf,ldif}{,.default}')
	self.cmd_run("install -v -dm700 -o ldap -g ldap /var/lib/openldap")
	self.cmd_run("install -v -dm700 -o ldap -g ldap /etc/openldap/slapd.d")
	self.cmd_run("chmod -v 640 /etc/openldap/slapd.{conf,ldif}")
	self.cmd_run("chown -v root:ldap /etc/openldap/slapd.{conf,ldif}")
	self.cmd_run(f"install -v -dm755 /usr/share/doc/openldap-{self.version}")
	self.cmd_run(
		 "cp -vfr doc/{drafts,rfc,guide}"
		f" /usr/share/doc/openldap-{self.version}"
	)
