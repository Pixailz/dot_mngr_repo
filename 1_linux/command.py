#!/usr/bin/env python3

from dot_mngr import *

def configure_kernel(self):
	self.kernel.config("WERROR", "n")
	self.kernel.config("PSI", "y")
	self.kernel.config("PSI_DEFAULT_DISABLED", "n")
	self.kernel.config("IKHEADERS", "n")
	self.kernel.config("CGROUPS", "y")
	self.kernel.config("MEMCG", "y")
	self.kernel.config("GROUP_SCHED", "y")
	self.kernel.config("RT_GROUP_SCHED", "n")
	self.kernel.config("EXPERT", "n")

	self.kernel.config("RELOCATABLE", "y")
	self.kernel.config("RANDOMIZE_BASE", "y")

	self.kernel.config("STACKPROTECTOR", "y")
	self.kernel.config("STACKPROTECTOR_STRONG", "y")

	self.kernel.config("NET", "y")
	self.kernel.config("INET", "y")
	self.kernel.config("IPV6", "y")

	self.kernel.config("UEVENT_HELPER", "n")
	self.kernel.config("DEVTMPFS", "y")
	self.kernel.config("DEVTMPFS_MOUNT", "y")

	self.kernel.config("FW_LOADER", "y")
	self.kernel.config("FW_LOADER_USER_HELPER", "n")
	self.kernel.config("DMIID", "y")

	self.kernel.config("DRM", "y")
	self.kernel.config("DRM_FBDEV_EMULATION", "y")
	self.kernel.config("FRAMEBUFFER_CONSOLE", "y")

	self.kernel.config("INOTIFY_USER", "y")
	self.kernel.config("TMPFS", "y")
	self.kernel.config("TMPFS_POSIX_ACL", "y")

	self.kernel.config("X86_X2APIC", "y")
	self.kernel.config("PCI", "y")
	self.kernel.config("PCI_MSI", "y")
	self.kernel.config("IOMMU_SUPPORT", "y")
	self.kernel.config("IRQ_REMAP", "y")

	self.kernel.config("HIGHMEM64G", "y")
	self.kernel.config("BLK_DEV_NVME", "y")
