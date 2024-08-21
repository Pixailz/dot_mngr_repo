#!/usr/bin/env python3

from dot_mngr import *

def install(self):
	self.chroot()
	self.cmd_run("/usr/sbin/make-ca -g")
	self.cmd_run("systemctl enable update-pki.timer")
	self.cmd_run("mkdir -pv /etc/profile.d")
	self.cmd_run(
		"""
		cat > /etc/profile.d/pythoncerts.sh <<-EOF
		# Begin /etc/profile.d/pythoncerts.sh

		export _PIP_STANDALONE_CERT=/etc/pki/tls/certs/ca-bundle.crt

		# End /etc/profile.d/pythoncerts.sh
		EOF
		"""
	)
