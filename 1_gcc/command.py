#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.cmd_run("echo ${PATH}")
	extract_file_from_package("1_mpfr", self.tar_folder)
	extract_file_from_package("1_gmp", self.tar_folder)
	extract_file_from_package("1_mpc", self.tar_folder)
	self.cmd_run("rm -rf mpfr; mv mpfr-* mpfr")
	self.cmd_run("rm -rf gmp; mv gmp-* gmp")
	self.cmd_run("rm -rf mpc; mv mpc-* mpc")

	match ARCH:
		case "x86_64":
			self.cmd_run(
				"sed -e '/m64=/s/lib64/lib/' -i.orig gcc/config/i386/t-linux64"
			)

	self.take_build()
	self.cmd_run(
		f"../configure"
		f" --target={TARGET_TRIPLET}"
		f" --prefix={PREFIX}/tools"
		f" --with-glibc-version={get_version_from_package('1_glibc')}"
		f" --with-sysroot={PREFIX}"
		 " --with-newlib"
		 " --without-headers"
		 " --enable-default-pie"
		 " --enable-default-ssp"
		 " --disable-nls"
		 " --disable-shared"
		 " --disable-multilib"
		 " --disable-threads"
		 " --disable-libatomic"
		 " --disable-libgomp"
		 " --disable-libquadmath"
		 " --disable-libssp"
		 " --disable-libvtv"
		 " --disable-libstdcxx"
		 " --enable-languages=c,c++"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	pass

def install(self):
	self.cmd_run("make install")
	os.chdir(self.tar_folder)
	self.cmd_run(
		 "cat gcc/limitx.h gcc/glimits.h gcc/limity.h >"
		f" \"$(dirname \"$(\"{TARGET_TRIPLET}-gcc\" -print-libgcc-file-name)\")\""
		 "/include/limits.h"
	)

def uninstall(self):
	pass
