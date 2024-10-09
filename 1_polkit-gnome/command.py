#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.download_patch("consolidated_fixes")
	self.chroot()
	self.apply_patch("consolidated_fixes", "-Np1")
	self.cmd_run(
		 "./configure"
		f" --prefix={PREFIX}"
	)

def compile(self):
	self.cmd_run("make")

def install(self):
	self.cmd_run("make install")
	self.cmd_run("mkdir -p /etc/xdg/autostart")
	self.cmd_run(
		 'cat << EOF > /etc/xdg/autostart/polkit-gnome-authentication-agent-1.desktop\n'
		 "[Desktop Entry]\n"
		 "Name=PolicyKit Authentication Agent\n"
		 "Comment=PolicyKit Authentication Agent\n"
		f"Exec={PREFIX}/libexec/polkit-gnome-authentication-agent-1\n"
		 "Terminal=false\n"
		 "Type=Application\n"
		 "Categories=\n"
		 "NoDisplay=true\n"
		 "OnlyShowIn=GNOME;XFCE;Unity;\n"
		 "AutostartCondition=GNOME3 unless-session gnome\n"
		 "EOF"
	)