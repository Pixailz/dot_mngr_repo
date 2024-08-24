#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	download_package(self, "sqlite-doc")
	self.chroot()
	sqlite_doc = get_package_from_name("sqlite-doc")
	self.cmd_run(f"unzip -q /sources/{sqlite_doc.file_name}")
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
		 " --disable-static"
		 " --enable-fts{4,5}"
		 ' CPPFLAGS="-D SQLITE_ENABLE_COLUMN_METADATA=1'
		 "           -D SQLITE_ENABLE_UNLOCK_NOTIFY=1"
		 "           -D SQLITE_ENABLE_DBSTAT_VTAB=1"
		 '           -D SQLITE_SECURE_DELETE=1"'
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install")
	major = self.version[0]
	minor = self.version[1:3].rstrip("0")
	patch = self.version[4:6].rstrip("0")
	version = f"{major}.{minor}.{patch}"
	self.cmd_run(f"install -v -m755 -d {PREFIX}/share/doc/sqlite-{version}")
	self.cmd_run(
		 "cp -v -R sqlite-doc-3460100/*"
		f" {PREFIX}/share/doc/sqlite-{version}"
	)