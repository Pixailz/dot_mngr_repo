#!/usr/bin/env python3

from dot_mngr import *

def configure_kernel(self):
	self.kernel.config("NET", "y")
	self.kernel.config("NETFILTER", "y")
	self.kernel.config("NETFILTER_ADVANCED", "y")
	self.kernel.config("NF_CONNTRACK", "y")
	self.kernel.config("NETFILTER_XT_TARGET_LOG", "y")
	self.kernel.config("IP_NF_IPTABLES", "y")
