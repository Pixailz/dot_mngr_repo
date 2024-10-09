#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.take_build()
	self.cmd_run(
		 "meson setup .."
		f" --prefix={PREFIX}"
		 " --buildtype=release"
		 " -D man=true"
		 " -D broadwy_backend=true"
	)

def compile(self):
	self.cmd_run("ninja")

def install(self):
	self.cmd_run("ninja install")
	self.cmd_run("mkdir -vp ~/.config/gtk-3.0")
	self.cmd_run(
		 'cat << "EOF" > ~/.config/gtk-3.0/settings.ini\n'
		 "[Settings]\n"
		 "gtk-theme-name = Adwaita\n"
		 "gtk-icon-theme-name = oxygen\n"
		 "gtk-font-name = DejaVu Sans 12\n"
		 "gtk-cursor-theme-size = 18\n"
		 "gtk-toolbar-style = GTK_TOOLBAR_BOTH_HORIZ\n"
		 "gtk-xft-antialias = 1\n"
		 "gtk-xft-hinting = 1\n"
		 "gtk-xft-hintstyle = hintslight\n"
		 "gtk-xft-rgba = rgb\n"
		 "gtk-cursor-theme-name = Adwaita\n"
		 "EOF"
	)
	self.cmd_run(
		 'cat << "EOF" > ~/.config/gtk-3.0/gtk.css\n'
		 "*  {\n"
   		 "    -GtkScrollbar-has-backward-stepper: 1;\n"
         "    -GtkScrollbar-has-forward-stepper: 1;\n"
         "}"
		 "EOF"
	)