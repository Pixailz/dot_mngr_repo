#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.add_path(f"{PREFIX}/tools/bin")
	self.add_env({
		"LC_ALL": "POSIX",
		"CONFIG_SITE": f"{PREFIX}/usr/share/config.site"
	})
	self.apply_patch("glibc-2.39-fhs-1", "-Np1")
	self.take_build()
	self.cmd_run(
		 "echo 'rootsbindir=/usr/sbin' > configparms &&"
		 " ../configure"
		 " --prefix=/usr"
		f" --host={TARGET_TRIPLET}"
		 " --build=$(../scripts/config.guess)"
		 " --enable-kernel=4.19"
		f" --with-headers={PREFIX}/usr/include"
		 " --disable-nscd"
		 " libc_cv_slibdir=/usr/lib"
	)

def compile(self):
	self.cmd_run("make", 1)

def install(self):
	self.cmd_run(
		f'make DESTDIR="{PREFIX}" install && '
		f"""sed '/RTLDLIST=/s@/usr@@g' -i "{PREFIX}/usr/bin/ldd" """
	)
	self.cmd_run("echo 'int main(){}' | " f'"{TARGET_TRIPLET}-gcc" -xc -')
	self.cmd_run("readelf -l a.out | grep ld-linux; rm -rf a.out")
