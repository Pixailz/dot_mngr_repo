#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run("sed '20,$ d' -i trust/trust-extract-compat")
	self.cmd_run(
		"""
		cat >> trust/trust-extract-compat <<-EOF
		# Copy existing anchor modifications to /etc/ssl/local
		/usr/libexec/make-ca/copy-trust-modification

		# Updates trust stores
		/usr/sbin/make-ca -r
		EOF
		"""
	)
	Os.take("p11-build")
	self.cmd_run(
		 "meson setup .."
		 " --prefix=/usr"
		 " --buildtype=release"
		 " -Dtrust_paths=/etc/pki/anchors"
	)

def compile(self):
	self.cmd_run("ninja")

def check(self):
	self.cmd_run("LC_ALL=C ninja test")

def install(self):
	self.cmd_run("ninja install")
	self.cmd_run(
		 "ln -sfv /usr/libexec/p11-kit/trust-extract-compat"
		 " /usr/bin/update-ca-certificates"
	)
	self.cmd_run("ln -sfv ./pkcs11/p11-kit-trust.so /usr/lib/libnssckbi.so")
