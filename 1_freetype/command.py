#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	download_package(self, "freetype-doc")
	self.chroot()
	freetype_doc = conf.get_package("freetype-doc")
	self.cmd_run(
		f"tar -xf {self.chrooted_get_path(freetype_doc.file_path, self.chrooted)}"
		 " --strip-components=2 -C docs"
	)

	self.cmd_run('sed -ri "s:.*(AUX_MODULES.*valid):\\1:" modules.cfg')
	self.cmd_run(
		 'sed -r "s:.*(#.*SUBPIXEL_RENDERING) .*:\\1:"'
		 " -i include/freetype/config/ftoption.h"
	)

	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --enable-freetype-config"
		 " --disable-static"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(f"cp -v -R docs -T {PREFIX}/share/doc/freetype-{self.version}")
	self.cmd_run(f"rm -v {PREFIX}/share/doc/freetype-{self.version}/freetype-config.1")