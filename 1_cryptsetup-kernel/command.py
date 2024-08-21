#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run("make mrproper && make defconfig")
	config_dest = f"/sources/{os.path.basename(self.tar_folder)}/.config"
	config_source = f"/boot/config-{self.version}"
	self.cmd_run(f"cp -fv {config_source} {config_dest}")
	kernel = Kernel(config_dest)

	kernel.config("MD", "y")
	kernel.config("BLK_DEV_DM", "y")
	kernel.config("DM_CRYPT", "y")
	kernel.config("CRYPTO", "y")
	kernel.config("CRYPTO_AES", "y")
	kernel.config("CRYPTO_TWOFISH", "y")
	kernel.config("CRYPTO_XTS", "y")
	kernel.config("CRYPTO_SHA256", "y")
	kernel.config("CRYPTO_USER_API_SKCIPHER", "y")

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
	self.cmd_run(f"rm -rf /usr/src/kernel-{self.version}")
	self.cmd_run(
		f'mv "/usr/src/{os.path.basename(self.tar_folder)}"'
		f' "/usr/src/kernel-{self.version}"'
	)
