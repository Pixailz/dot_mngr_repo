#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	match ARCH:
		case "x86_64":
			self.cmd_run(
				"sed -e '/m64=/s/lib64/lib/' -i.orig gcc/config/i386/t-linux64"
			)
	self.take_build()
	self.cmd_run(
		 "../configure"
		f" --prefix={PREFIX}"
		 " LD=ld"
		 " --enable-languages=c,c++"
		 " --enable-default-pie"
		 " --enable-default-ssp"
		 " --enable-host-pie"
		 " --disable-multilib"
		 " --disable-bootstrap"
		 " --disable-fixincludes"
		 " --with-system-zlib"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("ulimit -s 32768 && ulimit -f 1000000")
	self.cmd_run("sed -e '/cpython/d' -i ../gcc/testsuite/gcc.dg/plugin/plugin.exp")
	self.cmd_run("sed -e 's/no-pic /&-no-pie /' -i ../gcc/testsuite/gcc.target/i386/pr113689-1.c")
	self.cmd_run("sed -e 's/300000/(1|300000)/' -i ../libgomp/testsuite/libgomp.c-c++-common/pr109062.c")
	self.cmd_run(
		 "sed -e 's/{ target nonpic } //' "
		 " -e '/GOTPCREL/d' -i ../gcc/testsuite/gcc.target/i386/fentryname3.c"
	)
	self.cmd_run(
		 "chown -R tester . &&"
		 " su tester -c 'PATH=${PATH} make -k check || true'"
	)
	self.cmd_run("../contrib/test_summary | grep -A7 Summ | grep -v '^#'")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(
		f"chown -v -R root:root {PREFIX}/lib/gcc/$(gcc -dumpmachine)/{self.version}"
		 "/include{,-fixed}"
	)
	self.cmd_run(f"ln -sfvr {PREFIX}/bin/cpp {PREFIX}/lib")
	self.cmd_run(f"ln -sfv gcc.1 {PREFIX}/share/man/man1/cc.1")
	self.cmd_run(
		f"ln -sfv ../../libexec/gcc/$(gcc -dumpmachine)/{self.version}"
		f"/liblto_plugin.so {PREFIX}/lib/bfd-plugins/"
	)
	self.cmd_run("echo 'int main(){}' > dummy.c")
	self.cmd_run("cc dummy.c -v -Wl,--verbose &> dummy.log")
	self.cmd_run("readelf -l a.out | grep ': /lib'")
	self.cmd_run(f"grep -E -o '{PREFIX}/lib.*/S?crt[1in].*succeeded' dummy.log")
	self.cmd_run(f"grep -B4 '^ {PREFIX}/include' dummy.log")
	self.cmd_run(f"grep 'SEARCH.*{PREFIX}/lib' dummy.log | sed 's|; |\\n|g'")
	self.cmd_run("grep '/lib.*/libc.so.6 ' dummy.log")
	self.cmd_run("grep found dummy.log")
	self.cmd_run("rm -v dummy.{c,log} a.out")
	self.cmd_run(f"mkdir -pv {PREFIX}/share/gdb/auto-load{PREFIX}/lib")
	self.cmd_run(f"mv -v {PREFIX}/lib/*gdb.py {PREFIX}/share/gdb/auto-load{PREFIX}/lib")
