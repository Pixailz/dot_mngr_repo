#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.download_patch("nss-3.103-standalone-1")
	self.chroot()
	self.apply_patch("nss-3.103-standalone-1", "-Np1")
	Os.take("nss")

def compile(self):
	self.cmd_run(
		 "make"
		 " BUILD_OPT=1"
		f" NSPR_INCLUDE_DIR={PREFIX}/include/nspr"
		 " USE_SYSTEM_ZLIB=1"
		 " ZLIB_LIBS=-lz"
		 " NSS_ENABLE_WERROR=0"
		f" $([ {ARCH} == 'x86_64' ] && echo USE_64=1)"
		f" $([ -f {PREFIX}/include/sqlite3.h ] && echo NSS_USE_SYSTEM_SQLITE=1)"
	)

# def check(self):
# 	Os.take("tests")
# 	self.cmd_run("HOST=localhost DOMSUF=localdomain ./all.sh")
# 	Os.take("..")

def install(self):
	Os.take("../dist")
	self.cmd_run(f"install -v -m755 Linux*/lib/*.so {PREFIX}/lib ")
	self.cmd_run(
		 "install -v -m644 Linux*/lib/{*.chk,libcrmf.a}"
		f" {PREFIX}/lib"
	)
	self.cmd_run(f"install -v -m755 -d {PREFIX}/include/nss")
	self.cmd_run(
		 "cp -v -RL {public,private}/nss/*"
		f" {PREFIX}/include/nss"
	)
	self.cmd_run(
		 "install -v -m755 Linux*/bin/{certutil,nss-config,pk12util}"
		f" {PREFIX}/bin"
	)
	self.cmd_run(
		f"install -v -m644 Linux*/lib/pkgconfig/nss.pc {PREFIX}/lib/pkgconfig"
	)

	if conf.is_installed("1_p11-kit", False):
		self.cmd_run(
			f"ln -sfv ./pkcs11/p11-kit-trust.so {PREFIX}/lib/libnssckbi.so"
		)

