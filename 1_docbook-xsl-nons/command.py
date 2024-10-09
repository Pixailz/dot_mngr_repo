#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.download_patch("docbook-xsl-nons-stack_fix-1")
	download_package(self, "docbook-xsl-nons-doc")
	self.chroot()
	self.apply_patch("docbook-xsl-nons-stack_fix-1", "-Np1")
	docbook_xls_nons_doc = conf.get_package("docbook-xsl-nons-doc")
	docbook_xls_nons_doc.prepare_archive(chroot = self.chrooted)
	self.cmd_run(
		f"tar -xvf {self.chrooted_get_path(docbook_xls_nons_doc.file_path, self.chrooted)}"
		 " --strip-components=1"
	)
	self.cmd_run(
		 "install -v -m755 -d"
		f" {PREFIX}/share/xml/docbook/xsl-stylesheets-nons-{self.version}"
	)

def compile(self):
	self.cmd_run(
		 "cp -v -R VERSION assembly common eclipse epub epub3 extensions fo"
		 " highlighting html htmlhelp images javahelp lib manpages params"
		 " profiling roundtrip slides template tests tools webhelp website"
		 " xhtml xhtml-1_1 xhtml5"
		f" {PREFIX}/share/xml/docbook/xsl-stylesheets-nons-{self.version}"
	)
	self.cmd_run(
		f"ln -fs VERSION {PREFIX}/share/xml/docbook/"
		f"xsl-stylesheets-nons-{self.version}/VERSION.xsl"
	)
	self.cmd_run(
		 "install -v -m644 -D README"
		f" {PREFIX}/share/doc/docbook-xsl-nons-{self.version}/README.txt"
	)
	self.cmd_run(
		 "install -v -m644 RELEASE-NOTES* NEWS*"
		f" {PREFIX}/share/doc/docbook-xsl-nons-{self.version}"
	)
	self.cmd_run(f"cp -v -R doc/* {PREFIX}/share/doc/docbook-xsl-nons-{self.version}")

def install(self):
	if not os.path.isdir("/etc/xml"):
		self.cmd_run("install -v -d -m755 /etc/xml")
	if os.path.isfile("/etc/xml/catalog"):
		self.cmd_run("sed -i '/rewrite/d' /etc/xml/catalog")
	else:
		self.cmd_run("xmlcatalog --noout --create /etc/xml/catalog")
	self.cmd_run(
		 'xmlcatalog --noout --add "rewriteSystem"'
		f' "http://cdn.docbook.org/release/xsl-nons/{self.version}"'
		f' "{PREFIX}/share/xml/docbook/xsl-stylesheets-nons-{self.version}"'
		 " /etc/xml/catalog"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "rewriteSystem"'
		f' "https://cdn.docbook.org/release/xsl-nons/{self.version}"'
		f' "{PREFIX}/share/xml/docbook/xsl-stylesheets-nons-{self.version}"'
		 " /etc/xml/catalog"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "rewriteURI"'
		f' "http://cdn.docbook.org/release/xsl-nons/{self.version}"'
		f' "{PREFIX}/share/xml/docbook/xsl-stylesheets-nons-{self.version}"'
		 " /etc/xml/catalog"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "rewriteURI"'
		f' "https://cdn.docbook.org/release/xsl-nons/{self.version}"'
		f' "{PREFIX}/share/xml/docbook/xsl-stylesheets-nons-{self.version}"'
		 " /etc/xml/catalog"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "rewriteURI"'
		f' "http://cdn.docbook.org/release/xsl-nons/{self.version}"'
		f' "{PREFIX}/share/xml/docbook/xsl-stylesheets-nons-{self.version}"'
		 " /etc/xml/catalog"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "rewriteSystem"'
		f' "http://cdn.docbook.org/release/xsl-nons/current"'
		f' "{PREFIX}/share/xml/docbook/xsl-stylesheets-nons-{self.version}"'
		 " /etc/xml/catalog"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "rewriteSystem"'
		f' "https://cdn.docbook.org/release/xsl-nons/current"'
		f' "{PREFIX}/share/xml/docbook/xsl-stylesheets-nons-{self.version}"'
		 " /etc/xml/catalog"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "rewriteURI"'
		f' "http://cdn.docbook.org/release/xsl-nons/current"'
		f' "{PREFIX}/share/xml/docbook/xsl-stylesheets-nons-{self.version}"'
		 " /etc/xml/catalog"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "rewriteURI"'
		f' "https://cdn.docbook.org/release/xsl-nons/current"'
		f' "{PREFIX}/share/xml/docbook/xsl-stylesheets-nons-{self.version}"'
		 " /etc/xml/catalog"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "rewriteSystem"'
		f' "http://docbook.sourceforge.net/release/xsl/current"'
		f' "{PREFIX}/share/xml/docbook/xsl-stylesheets-nons-{self.version}"'
		 " /etc/xml/catalog"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "rewriteURI"'
		f' "http://docbook.sourceforge.net/release/xsl/current"'
		f' "{PREFIX}/share/xml/docbook/xsl-stylesheets-nons-{self.version}"'
		 " /etc/xml/catalog"
	)