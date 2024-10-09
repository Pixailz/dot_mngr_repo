#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run("sed '20,$ d' -i trust/trust-extract-compat")
	self.cmd_run(
		 "cat >> trust/trust-extract-compat <<EOF\n"
		 "# Copy existing anchor modifications to /etc/ssl/local\n"
		f"{PREFIX}/libexec/make-ca/copy-trust-modification\n"
		 "\n"
		 "# Updates trust stores\n"
		f"{PREFIX}/sbin/make-ca -r\n"
		 "EOF"
	)
	Os.take("p11-build")
	self.cmd_run(
		 "meson setup .."
		f" --prefix={PREFIX}"
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
		f"ln -sfv {PREFIX}/libexec/p11-kit/trust-extract-compat"
		f" {PREFIX}/bin/update-ca-certificates"
	)
	self.cmd_run(f"ln -sfv ./pkcs11/p11-kit-trust.so {PREFIX}/lib/libnssckbi.so")
