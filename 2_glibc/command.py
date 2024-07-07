#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.download_patch("glibc-2.39-fhs-1")
	download_package(self, "1_tzdata")
	self.chroot()
	self.apply_patch("glibc-2.39-fhs-1", "-Np1")
	self.take_build()
	self.cmd_run(
		 "echo 'rootsbindir=/usr/sbin' > configparms &&"
		 " ../configure"
		 " --prefix=/usr"
		 " --disable-werror"
		 " --enable-kernel=4.19"
		 " --enable-stack-protector=strong"
		 " --disable-nscd"
		 " libc_cv_slibdir=/usr/lib"
	)

def compile(self):
	self.cmd_run("make")

# def check(self):
# 	self.cmd_run("make check")

def install(self):
	self.cmd_run(
		 "touch /etc/ld.so.conf &&"
		 " sed '/test-installation/s@\\$(PERL)@echo not running@' -i ../Makefile &&"
		 " make install &&"
		 " sed '/RTLDLIST=/s@/usr@@g' -i /usr/bin/ldd &&"
		 " mkdir -pv /usr/lib/locale &&"
		 " localedef -i C      -f UTF-8       C.UTF-8 &&"
		 " localedef -i cs_CZ  -f UTF-8       cs_CZ.UTF-8 &&"
		 " localedef -i de_DE  -f ISO-8859-1  de_DE &&"
		 " localedef -i de_DE@euro -f ISO-8859-15 de_DE@euro &&"
		 " localedef -i de_DE -f UTF-8 de_DE.UTF-8 &&"
		 " localedef -i el_GR -f ISO-8859-7 el_GR &&"
		 " localedef -i en_GB -f ISO-8859-1 en_GB &&"
		 " localedef -i en_GB -f UTF-8 en_GB.UTF-8 &&"
		 " localedef -i en_HK -f ISO-8859-1 en_HK &&"
		 " localedef -i en_PH -f ISO-8859-1 en_PH &&"
		 " localedef -i en_US -f ISO-8859-1 en_US &&"
		 " localedef -i en_US -f UTF-8 en_US.UTF-8 &&"
		 " localedef -i es_ES -f ISO-8859-15 es_ES@euro &&"
		 " localedef -i es_MX -f ISO-8859-1 es_MX &&"
		 " localedef -i fa_IR -f UTF-8 fa_IR &&"
		 " localedef -i fr_FR -f ISO-8859-1 fr_FR &&"
		 " localedef -i fr_FR@euro -f ISO-8859-15 fr_FR@euro &&"
		 " localedef -i fr_FR -f UTF-8 fr_FR.UTF-8 &&"
		 " localedef -i is_IS -f ISO-8859-1 is_IS &&"
		 " localedef -i is_IS -f UTF-8 is_IS.UTF-8 &&"
		 " localedef -i it_IT -f ISO-8859-1 it_IT &&"
		 " localedef -i it_IT -f ISO-8859-15 it_IT@euro &&"
		 " localedef -i it_IT -f UTF-8 it_IT.UTF-8 &&"
		 " localedef -i ja_JP -f EUC-JP ja_JP &&"
		 " localedef -i ja_JP -f UTF-8 ja_JP.UTF-8 &&"
		 " localedef -i nl_NL@euro -f ISO-8859-15 nl_NL@euro &&"
		 " localedef -i ru_RU -f KOI8-R ru_RU.KOI8-R &&"
		 " localedef -i ru_RU -f UTF-8 ru_RU.UTF-8 &&"
		 " localedef -i se_NO -f UTF-8 se_NO.UTF-8 &&"
		 " localedef -i ta_IN -f UTF-8 ta_IN.UTF-8 &&"
		 " localedef -i tr_TR -f UTF-8 tr_TR.UTF-8 &&"
		 " localedef -i zh_CN -f GB18030 zh_CN.GB18030 &&"
		 " localedef -i zh_HK -f BIG5-HKSCS zh_HK.BIG5-HKSCS &&"
		 " localedef -i zh_TW -f UTF-8 zh_TW.UTF-8"
	)
	extract_file_from_package("1_tzdata", os.path.join(self.tar_folder, "build"), self.chrooted)
	self.cmd_run(
		"export ZONEINFO=/usr/share/zoneinfo && "
		" mkdir -pv ${ZONEINFO}/{posix,right} && "
		" for tz in etcetera southamerica northamerica europe africa antarctica asia australasia backward; do "
		" zic -L /dev/null -d ${ZONEINFO} ${tz} && "
		" zic -L /dev/null -d ${ZONEINFO}/posix ${tz} && "
		" zic -L leapseconds -d ${ZONEINFO}/right ${tz}; done && "
		" cp -v zone.tab zone1970.tab iso3166.tab ${ZONEINFO} && "
		" zic -d ${ZONEINFO} -p America/New_York"
	)
	# self.cmd_run(
	# 	"export ZONEINFO=/usr/share/zoneinfo && "
	# 	" mkdir -pv ${ZONEINFO}/{posix,right} && "
	# 	" for tz in etcetera southamerica northamerica europe africa antarctica asia australasia backward pacificnew systemv; do "
	# 	" zic -L /dev/null -d ${ZONEINFO} ${tz} && "
	# 	" zic -L /dev/null -d ${ZONEINFO}/posix ${tz} && "
	# 	" zic -L leapseconds -d ${ZONEINFO}/right ${tz}; done && "
	# 	" cp -v zone.tab zone1970.tab iso3166.tab ${ZONEINFO} && "
	# 	" zic -d ${ZONEINFO} -p America/New_York"
	# )
	self.unchroot()
