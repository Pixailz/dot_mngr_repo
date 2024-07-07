#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.add_path(f"{PREFIX}/tools/bin")
	self.add_env({
		"LC_ALL": "POSIX",
		"CONFIG_SITE": f"{PREFIX}/usr/share/config.site"
	})
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
	self.cmd_run(
		"sed '/thread_header =/s/@.*@/gthr-posix.h/'"
		" -i libgcc/Makefile.in libstdc++-v3/include/Makefile.in"
	)
	self.take_build()
	self.cmd_run(
		 "../configure"
		 ' --build="$(../config.guess)"'
		f" --host={TARGET_TRIPLET}"
		f" --target={TARGET_TRIPLET}"
		f' LDFLAGS_FOR_TARGET="-L{self.tar_folder}/{TARGET_TRIPLET}/libgcc"'
		 " --prefix=/usr"
		f" --with-build-sysroot={PREFIX}"
		 " --enable-default-pie"
		 " --enable-default-ssp"
		 " --disable-nls"
		 " --disable-multilib"
		 " --disable-libatomic"
		 " --disable-libgomp"
		 " --disable-libquadmath"
		 " --disable-libsanitizer"
		 " --disable-libssp"
		 " --disable-libvtv"
		 " --enable-languages=c,c++"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.take_build()
	self.cmd_run(f'make DESTDIR="{PREFIX}" install')
	if not os.path.exists(f"{PREFIX}/usr/bin/cc"):
		self.cmd_run(f"ln -s gcc {PREFIX}/usr/bin/cc")
