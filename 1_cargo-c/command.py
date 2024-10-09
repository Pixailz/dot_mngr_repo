#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(
		 "curl -LO https://github.com/lu-zero/cargo-c/releases/download/"
		f"v{self.version}/Cargo.lock"
	)

def compile(self):
	libssh2 = "0"
	sqlite = "0"
	if conf.is_installed("1_libssh2", False):
		libssh2 = "1"
	if conf.is_installed("1_sqlite", False):
		sqlite = "1"
	self.cmd_run(
		 "export"
		f" LIBSSH2_SYS_USE_PKG_CONFIG={libssh2}"
		f" LIBSQLITE3_SYS_USE_PKG_CONFIG={sqlite}"
		 " &&"
		 "   cargo build --release"
	)

def check(self):
	self.cmd_run("cargo test --release")

def install(self):
	self.cmd_run(
		 "install -vm755 target/release/cargo-{capi,cbuild,cinstall,ctest}"
		f" {PREFIX}/bin/"
	)
