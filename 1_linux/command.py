#!/usr/bin/env python3

from dot_mngr import *

class Kernel():

	def __init__(self, conf_path):
		self.conf_path = conf_path

	def config(self, key, value, prefix="CONFIG_"):
		with open(self.conf_path, "r") as f:
			file_str = f.read()

		if prefix + key not in file_str:
			file_str += f"# {prefix}{key} is not set\n"

		pre_key = f"{prefix}{key}"
		file_str = re.sub(
			r".*" + re.escape(f"{pre_key}") + r"[ =].*",
			f"{pre_key}={value}",
			file_str
		)

		with open(self.conf_path, "w") as f:
			f.write(file_str)

def configure(self):
	self.chroot()
	self.cmd_run(
		 "make mrproper &&"
		 " make defconfig"
	)

	kernel = Kernel(f"/sources/{os.path.basename(self.tar_folder)}/.config")

	kernel.config("WERROR", "n")
	kernel.config("PSI", "y")
	kernel.config("PSI_DEFAULT_DISABLED", "n")
	kernel.config("IKHEADERS", "n")
	kernel.config("CGROUPS", "y")
	kernel.config("MEMCG", "y")
	kernel.config("EXPERT", "n")

	kernel.config("RELOCATABLE", "y")
	kernel.config("RANDOMISE_BASE", "y")

	kernel.config("STACKPROTECTOR", "y")
	kernel.config("STACKPROTECTOR_STRONG", "y")

	kernel.config("UEVENT_HELPER", "n")
	kernel.config("DEVTMPFS", "y")
	kernel.config("DEVTMPFS_MOUNT", "y")

	kernel.config("DRM", "y")
	kernel.config("DRM_FBDEV_EMULATION", "y")
	kernel.config("FRAMEBUFFER_CONSOLE", "y")

	kernel.config("X86_X2APIC", "y")
	kernel.config("PCI", "y")
	kernel.config("PCI_MSI", "y")
	kernel.config("IOMMU_SUPPORT", "y")
	kernel.config("IRQ_REMAP", "y")

	self.localversion = os.getenv("DISTRO_CODENAME")
	self.vmlinuz = os.getenv("VMLINUZ")

	print(f"{self.localversion = }")
	if self.localversion:
		kernel.config("LOCALVERSION", f'"-{self.localversion}"')
		kernel.config("LOCALVERSION_AUTO", "y")

	self.cmd_run(
		 "rm -rf"
		f" /boot/System.map-{self.version}"
		f" /boot/{self.vmlinuz}"
		f" /boot/config-{self.version}"
		f" /usr/share/doc/linux-{self.version}"
	)


def compile(self):
	self.cmd_run("yes '' | make")

def install(self):
	self.cmd_run("make modules_install")
	self.cmd_run(f"cp -fiv System.map /boot/System.map-{self.version}")
	self.cmd_run(f"cp -fiv arch/x86/boot/bzImage /boot/{self.vmlinuz}")
	self.cmd_run(f"cp -fiv .config /boot/config-{self.version}")
	self.cmd_run(f"cp -fr Documentation -T /usr/share/doc/linux-{self.version}")

	self.cmd_run(f"tar -xf /sources/{self.file_name} -C /usr/src")
	self.cmd_run(
		f'mv "/usr/src/{os.path.basename(self.tar_folder)}"'
		f' "/usr/src/kernel-{self.version}"'
	)
