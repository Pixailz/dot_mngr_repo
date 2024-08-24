#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.download_patch("coreutils-9.5-i18n-1")
	self.chroot()
	self.apply_patch("coreutils-9.5-i18n-1", "-Np1")
	# self.cmd_run("sed -e '/n_out += n_hold/,+4 s|.*bufsize.*|//&|' -i src/split.c")
	self.cmd_run("autoreconf -fiv")
	self.cmd_run(
		 "FORCE_UNSAFE_CONFIGURE=1 ./configure"
		f" --prefix={PREFIX}"
		 " --enable-no-install-program=kill,uptime"
	)

def compile(self):
	self.cmd_run("make")

# def check(self):
# 	self.cmd_run("make NON_ROOT_USERNAME=tester check-root")
# 	self.cmd_run("groupadd -g 102 dummy -U tester")
# 	self.cmd_run("chown -R tester .")
# 	self.cmd_run('su tester -c "PATH=$PATH make -k RUN_EXPENSIVE_TESTS=yes check" < /dev/null')
# 	self.cmd_run("groupdel dummy")

def install(self):
	self.cmd_run("make install")
	self.cmd_run(f"mv -v {PREFIX}/bin/chroot {PREFIX}/sbin")
	self.cmd_run(f"mv -v {PREFIX}/share/man/man1/chroot.1 {PREFIX}/share/man/man8/chroot.8")
	self.cmd_run("sed -i 's/\"1\"/\"8\"/' /usr/share/man/man8/chroot.8")
