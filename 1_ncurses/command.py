#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.add_path(f"{PREFIX}/tools/bin")
	self.add_env({
		"LC_ALL": "POSIX",
		"CONFIG_SITE": f"{PREFIX}/usr/share/config.site"
	})
	self.cmd_run("sed s/mawk// configure")
	self.take_build()
	self.cmd_run(
		"../configure && "
		"make -C include && "
		"make -C progs tic"
	)
	self.take_tar_folder()
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		f" --host={TARGET_TRIPLET}"
		 ' --build="$(./config.guess)"'
		 " --mandir=/usr/share/man"
		 " --with-manpage-format=normal"
		 " --with-shared"
		 " --without-normal"
		 " --with-cxx-shared"
		 " --without-debug"
		 " --without-ada"
		 " --disable-stripping"
		 " --enable-widec"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run(
		f'make DESTDIR="{PREFIX}"'
		f' TIC_PATH="{self.tar_folder}/build/progs/tic" install'
	)
	if not os.path.exists(f"{PREFIX}/usr/lib/libncurses.so"):
		self.cmd_run(f'ln -s libncursesw.so "{PREFIX}/usr/lib/libncurses.so"')
	self.cmd_run(
		 "sed -e 's/^#if.*XOPEN.*$/#if 1/' -i "
		f'"{PREFIX}/usr/include/curses.h"'
	)
