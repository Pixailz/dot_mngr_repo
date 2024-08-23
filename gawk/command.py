#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run("sed -i 's/extras//' Makefile.in")
	self.cmd_run(
		 "./configure"
		 " --prefix=/usr"
	)

def compile(self):
	self.cmd_run("make")

def check(self):
	self.cmd_run("chown -R tester .")
	self.cmd_run('su tester -c "PATH=${PATH} make check"')
	self.cmd_run(f"rm -f /usr/bin/gawk-{self.version}")

def install(self):
	self.cmd_run("make install")
	self.cmd_run("ln -sfv gawk.1 /usr/share/man/man1/awk.1")
	self.cmd_run(f"mkdir -pv /usr/share/doc/gawk-{self.version}")
	self.cmd_run(
		 "cp -v doc/{awkforai.txt,*.{eps,pdf,jpg}} "
		f"/usr/share/doc/gawk-{self.version}"
	)
