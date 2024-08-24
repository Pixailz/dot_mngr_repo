#!/usr/bin/env python3

from dot_mngr import *

def configure_kernel(self):
	self.kernel.config("BLK_DEV", "y")

	self.kernel.config("BLK_DEV_RAM", "y")

	self.kernel.config("MD", "y")
	self.kernel.config("BLK_DEV_DM", "y")
	self.kernel.config("DM_CRYPT", "y")
	self.kernel.config("DM_SNAPSHOT", "y")
	self.kernel.config("DM_THIN_PROVISIONING", "y")
	self.kernel.config("DM_CACHE", "y")
	self.kernel.config("DM_MIRROR", "y")
	self.kernel.config("DM_ZERO", "y")
	self.kernel.config("DM_DELAY", "y")

	self.kernel.config("MAGIC_SYSRQ", "y")
