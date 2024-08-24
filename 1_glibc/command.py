#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.add_path(f"{ROOT_PATH}/tools/bin")
	self.add_env({
		"LC_ALL": "POSIX",
		"CONFIG_SITE": f"{ROOT_PATH}{PREFIX}/share/config.site"
	})
	if ARCH == "x86_64":
		self.cmd_run(f"ln -sfv ../lib/ld-linux-x86-64.so.2 {ROOT_PATH}/lib64")
		self.cmd_run(f"ln -sfv ../lib/ld-linux-x86-64.so.2 {ROOT_PATH}/lib64/ld-lsb-x86-64.so.3")
	elif ARCH.startswith("i") and ARCH.endswith("86"):
		self.cmd_run(f"ln -sfv ld-linux.so.2 {ROOT_PATH}/lib/ld-lsb.so.3")

	self.apply_patch("glibc-2.40-fhs-1", "-Np1")
	self.take_build()
	self.cmd_run(f"echo 'rootsbindir={PREFIX}/sbin' > configparms")
	self.cmd_run(
		 " ../configure"
		f" --prefix={PREFIX}"
		f" --host={TARGET_TRIPLET}"
		 " --build=$(../scripts/config.guess)"
		 " --enable-kernel=4.19"
		f" --with-headers={ROOT_PATH}{PREFIX}/include"
		 " --disable-nscd"
		f" libc_cv_slibdir={PREFIX}/lib"
	)

def compile(self):
	self.cmd_run("make", 1)

def install(self):
	self.cmd_run(f"make DESTDIR={ROOT_PATH} install")
	self.cmd_run(f"sed '/RTLDLIST=/s@/{PREFIX}@@g' -i {ROOT_PATH}{PREFIX}/bin/ldd")
	self.cmd_run("echo 'int main(){}' | " f"{TARGET_TRIPLET}-gcc -xc -")
	self.cmd_run("readelf -l a.out | grep ld-linux; rm -rf a.out")
