#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	download_package(self, "nasm-doc")
	self.chroot()
	nasm_doc = conf.get_package("nasm-doc")
	self.cmd_run(
		f"tar -xvf {self.chrooted_get_path(nasm_doc.file_path, self.chrooted)}"
		 " --strip-components=1"
	)
	self.generate_configure()
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install || true")
	self.cmd_run(
		f"install -m755 -d {PREFIX}/share/doc/nasm-{self.version}/html"
	)
	self.cmd_run(
		 "cp -v doc/html/*.html"
		f" {PREFIX}/share/doc/nasm-{self.version}/html"
	)
	self.cmd_run(
		 "cp -v doc/*.{txt,ps,pdf}"
		f" {PREFIX}/share/doc/nasm-{self.version}"
	)