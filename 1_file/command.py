#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.add_path(f"{ROOT_PATH}/tools/bin")
	self.add_env({
		"LC_ALL": "POSIX",
		"CONFIG_SITE": f"{ROOT_PATH}{PREFIX}/share/config.site"
	})
	self.take_build()
	self.cmd_run(
		 "../configure"
		 " --disable-bzlib"
		 " --disable-libseccomp"
		 " --disable-xzlib"
		 " --disable-zlib && make"
	)
	self.take_archive_folder()
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		f" --host={TARGET_TRIPLET}"
		 " --build=$(./config.guess)"
	)

def compile(self):
	self.cmd_run(f"make FILE_COMPILE={self.archive_folder}/build/src/file")

def install(self):
	self.cmd_run(f"make DESTDIR={ROOT_PATH} install")
	self.cmd_run(f"rm -rf {ROOT_PATH}{PREFIX}/lib/libmagic.la")
