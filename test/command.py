#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	p.info("pass")
	self.chroot()
	p.info(f"{TARGET_TRIPLET = }")
	# self.add_path(f"{PREFIX}/tools/bin")
	# self.add_env({
	# 	"LC_ALL": "POSIX",
	# 	"CONFIG_SITE": f"{PREFIX}/usr/share/config.site"
	# })
	# self.chroot()
	# self.cmd_run("export")

	# download_package(self, "1_tzdata")
	# self.chroot()
	# # self.apply_patch("glibc-2.39-fhs-1", "-Np1")
	# self.take_build()
	# print("\nPASS\n")

	# extract_file_from_package("1_tzdata", os.path.join(self.tar_folder, "build"), self.chrooted)
