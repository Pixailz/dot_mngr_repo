#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.add_path(f"{PREFIX}/tools/bin")
	self.add_env({
		"LC_ALL": "POSIX",
		"CONFIG_SITE": f"{PREFIX}/usr/share/config.site"
	})
	self.take_build()
	self.cmd_run(
		 "../configure"
		 " --disable-bzlib"
		 " --disable-libseccomp"
		 " --disable-xzlib"
		 " --disable-zlib && make"
	)
	self.take_tar_folder()
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		f" --host={TARGET_TRIPLET}"
		 ' --build="$(./config.guess)"'
	)

def compile(self):
	self.cmd_run(f'make FILE_COMPILE={self.tar_folder}/build/src/file')

def install(self):
	self.cmd_run(
		f'make DESTDIR="{PREFIX}" install &&'
		f" rm -rf {PREFIX}/usr/lib/libmagic.la"
	)
