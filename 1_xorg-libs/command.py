#!/usr/bin/env python3

from dot_mngr import *

XORG_LIBS = [
	"xtrans",
	"libX11",
	"libXext",
	"libFS",
	"libICE",
	"libSM",
	"libXScrnSaver",
	"libXt",
	"libXmu",
	"libXpm",
	"libXaw",
	"libXfixes",
	"libXcomposite",
	"libXrender",
	"libXcursor",
	"libXdamage",
	"libfontenc",
	"libXfont2",
	"libXft",
	"libXi",
	"libXinerama",
	"libXrandr",
	"libXres",
	"libXtst",
	"libXv",
	"libXvMC",
	"libXxf86dga",
	"libXxf86vm",
	"libpciaccess",
	"libxkbfile",
	"libxshmfence",
	"libXpresent",
]

def	download_xorg_librairies(self):
	for pack in XORG_LIBS:
		download_package(self, pack)

def configure(self):
	download_xorg_librairies(self)

def compile(self):
	for pack in XORG_LIBS:
		_pack = conf.get_package(pack)
		_pack.prepare()
		_pack.chroot()

		doc_dir = f"--docdir={XORG_PREFIX}/share/doc/{_pack.name}-{_pack.version}"

		if _pack.name == "libXfont2":
			_pack.cmd_run(
					"./configure"
				f" {XORG_CONFIG}"
				f" {doc_dir}"
					" --disable-devel-docs"
			)
		elif _pack.name == "libXt":
			_pack.cmd_run(
					"./configure"
				f" {XORG_CONFIG}"
				f" {doc_dir}"
					" --with-appdefaultdir=/etc/X11/app-defaults"
			)
		elif _pack.name == "libXpm":
			_pack.cmd_run(
					"./configure"
				f" {XORG_CONFIG}"
				f" {doc_dir}"
					" --disable-open-zfile"
			)
		elif _pack.name == "libpciaccess":
			_pack.take_build()
			_pack.cmd_run("ls -la ..")
			_pack.cmd_run(
				"meson setup"
				f" --prefix={PREFIX}"
				" --buildtype=release"
				" .."
			)
			_pack.cmd_run("ninja")
			_pack.cmd_run("ninja install")
			_pack.unchroot()
			continue
		else:
			_pack.cmd_run(
					"./configure"
				f" {XORG_CONFIG}"
				f" {doc_dir}"
			)
		_pack.cmd_run("make")
		_pack.cmd_run("make install")
		_pack.unchroot()

def install(self):
	if PREFIX != XORG_PREFIX:
		self.cmd_run(f"ln -sv {XORG_PREFIX}/lib/X11 {PREFIX}/lib/X11")
		self.cmd_run(f"ln -sv {XORG_PREFIX}/include/X11 {PREFIX}/include/X11")