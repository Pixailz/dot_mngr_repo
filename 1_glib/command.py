#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.download_patch("glib-skip_warnings-1")
	download_package(self, "gobject-introspection")
	self.chroot()
	self.apply_patch("glib-skip_warnings-1", "-Np1")
	path = os.path.join(PREFIX, "include/glib-2.0")
	if os.path.isfile(path):
		self.cmd_run(f"rm -rf {path}.old")
		self.cmd_run(f"mv -vf {path}" "{,.old}")
	self.take_build()

	self.cmd_run(
		 "meson setup .."
		f" --prefix={PREFIX}"
		 " --buildtype=release"
		 " -D introspection=disabled"
		 " -D glib_debug=disabled"
		 " -D man-pages=enabled"
		 " -D sysprof=disabled"
	)

def compile(self):
	self.cmd_run("ninja")

def install(self):
	self.cmd_run("ninja install")
	gobject = conf.get_package("gobject-introspection")
	gobject.prepare_archive(chroot = self.chrooted)
	self.cmd_run(
		 "tar -xvf "
		f" {self.chrooted_get_path(gobject.file_path, self.chrooted)}"
	)
	self.cmd_run(
		f"meson setup {gobject.archive_folder} gi-build"
		f" --prefix={PREFIX}"
		 " --buildtype=release"
	)
	self.cmd_run("ninja -C gi-build")
	self.cmd_run("ninja -C gi-build install")
	self.cmd_run("meson configure -D introspection=enabled")
	self.cmd_run("ninja")
	self.cmd_run("ninja install")