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
		 " --prefix=/usr"
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
		 " su tester -c 'PATH=${PATH} make -k check || true"
	)
	self.cmd_run("../contrib/test_summary | grep -A7 Summ | grep -v '^#'")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(
		f"chown -v -R root:root /usr/lib/gcc/$(gcc -dumpmachine)/{self.version}"
		 "/include{,-fixed}"
	)
	self.cmd_run("ln -sfvr /usr/bin/cpp /usr/lib")
	self.cmd_run("ln -sfv gcc.1 /usr/share/man/man1/cc.1")
	self.cmd_run(
		f"ln -sfv ../../libexec/gcc/$(gcc -dumpmachine)/{self.version}"
		 "/liblto_plugin.so /usr/lib/bfd-plugins/"
	)
	self.cmd_run("echo 'int main(){}' > dummy.c")
	self.cmd_run("cc dummy.c -v -Wl,--verbose &> dummy.log")
	self.cmd_run("readelf -l a.out | grep ': /lib'")
	self.cmd_run("grep -E -o '/usr/lib.*/S?crt[1in].*succeeded' dummy.log")
	self.cmd_run("grep -B4 '^ /usr/include' dummy.log")
	self.cmd_run("grep 'SEARCH.*/usr/lib' dummy.log | sed 's|; |\\n|g'")
	self.cmd_run("grep '/lib.*/libc.so.6 ' dummy.log")
	self.cmd_run("grep found dummy.log")
	self.cmd_run("rm -v dummy.{c,log} a.out")
	self.cmd_run("mkdir -pv /usr/share/gdb/auto-load/usr/lib")
	self.cmd_run("mv -v /usr/lib/*gdb.py /usr/share/gdb/auto-load/usr/lib")
