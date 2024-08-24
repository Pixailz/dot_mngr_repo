#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	download_package(self, "1_cracklib-words")
	self.chroot()
	self.cmd_run("autoreconf -fiv")
	self.cmd_run(
		 "PYTHON=python3 ./configure"
		f" --prefix={PREFIX}"
		 " --disable-static"
		f" --with-default-dict={PREFIX}/lib/cracklib/pw_dict"
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
		f" {PREFIX}/share/dict/cracklib-words.xz"
	)
	if os.path.exists(f"{PREFIX}/share/dict/cracklib-words"):
		self.cmd_run(f"rm -v {PREFIX}/share/dict/cracklib-words")
	self.cmd_run(f"unxz -v {PREFIX}/share/dict/cracklib-words.xz")
	self.cmd_run(f"ln -v -sf cracklib-words {PREFIX}/share/dict/words")
	self.cmd_run(f"echo $(hostname) >> {PREFIX}/share/dict/cracklib-extra-words")
	self.cmd_run(f"install -v -m755 -d {PREFIX}/lib/cracklib")
	self.cmd_run(
		f"create-cracklib-dict {PREFIX}/share/dict/cracklib-words"
		f" {PREFIX}/share/dict/cracklib-extra-words"
	)
