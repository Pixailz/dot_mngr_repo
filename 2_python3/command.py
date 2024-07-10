#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	download_package(self, "1_python3-doc")
	self.chroot()
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
		 " --enable-shared"
		 " --with-system-expat"
		 " --enable-optimizations"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(f"install -v -dm755 /usr/share/doc/python-{self.version}/html")
	python3_doc = get_package_from_name("1_python3-doc")
	python3_doc.prepare_tarball(chroot=self.chrooted)
	tar_file = self.chrooted_get_path(python3_doc.file_path, self.chrooted)
	self.cmd_run(f"tar --no-same-owner -xvf {tar_file}")
	self.cmd_run(
		f"cp -R --no-preserve=mode {os.path.basename(python3_doc.tar_folder)}/*"
		f" /usr/share/doc/python-{self.version}/html"
	)
#