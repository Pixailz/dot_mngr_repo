#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	download_package(self, "1_cracklib-words")
	self.chroot()
	self.cmd_run("autoreconf -fiv")
	self.cmd_run(
		"PYTHON=python3 ./configure"
		" --prefix=/usr"
		" --disable-static"
		" --with-default-dict=/usr/lib/cracklib/pw_dict"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("make test")

def install(self):
	self.cmd_run("make install")
	cracklib_word = get_package_from_name("1_cracklib-words")
	self.cmd_run(
		f"install -v -m644 -D ../{cracklib_word.file_name}"
		 " /usr/share/dict/cracklib-words.xz"
	)
	if os.path.exists("/usr/share/dict/cracklib-words"):
		self.cmd_run("rm -v /usr/share/dict/cracklib-words")
	self.cmd_run("unxz -v /usr/share/dict/cracklib-words.xz")
	self.cmd_run("ln -v -sf cracklib-words /usr/share/dict/words")
	self.cmd_run("echo $(hostname) >> /usr/share/dict/cracklib-extra-words")
	self.cmd_run("install -v -m755 -d /usr/lib/cracklib")
	self.cmd_run(
		 "create-cracklib-dict /usr/share/dict/cracklib-words"
		 " /usr/share/dict/cracklib-extra-words"
	)
