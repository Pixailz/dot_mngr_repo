#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(f"install -v -d -m755 {PREFIX}/share/xml/docbook/xml-dtd-{self.version}")
	self.cmd_run(f"install -v -d -m755 /etc/xml")

def compile(self):
	self.cmd_run(
		 "cp -v -af --no-preserve=ownership docbook.cat *.dtd ent/ *.mod"
		f" {PREFIX}/share/xml/docbook/xml-dtd-{self.version}"
	)
	self.cmd_run(
		 "if [ ! -e /etc/xml/docbook ]; then"
		 " xmlcatalog --noout --create /etc/xml/docbook;"
		 " fi"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "public"'
		f' "-//OASIS//DTD DocBook XML V{self.version}//EN"'
		f' "http://www.oasis-open.org/docbook/xml/{self.version}/docbookx.dtd"'
		 " /etc/xml/docbook"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "public"'
		f' "-//OASIS//DTD DocBook XML CALS Table Model V{self.version}//EN"'
		f' "file://{PREFIX}/share/xml/docbook/xml-dtd-{self.version}/calstblx.dtd"'
		 " /etc/xml/docbook"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "public"'
		 ' "-//OASIS//DTD XML Exchange Table Model 19990315//EN"'
		f' "file://{PREFIX}/share/xml/docbook/xml-dtd-{self.version}/soextblx.dtd"'
		 " /etc/xml/docbook"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "public"'
		f' "-//OASIS//ELEMENTS DocBook XML Information Pool V{self.version}//EN"'
		f' "file://{PREFIX}/share/xml/docbook/xml-dtd-{self.version}/dbpoolx.mod"'
		 " /etc/xml/docbook"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "public"'
		f' "-//OASIS//ELEMENTS DocBook XML Document Hierarchy V{self.version}//EN"'
		f' "file://{PREFIX}/share/xml/docbook/xml-dtd-{self.version}/dbhierx.mod"'
		 " /etc/xml/docbook"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "public"'
		f' "-//OASIS//ELEMENTS DocBook XML HTML Tables V{self.version}//EN"'
		f' "file://{PREFIX}/share/xml/docbook/xml-dtd-{self.version}/htmltblx.mod"'
		 " /etc/xml/docbook"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "public"'
		f' "-//OASIS//ENTITIES DocBook XML Notations V{self.version}//EN"'
		f' "file://{PREFIX}/share/xml/docbook/xml-dtd-{self.version}/dbnotnx.mod"'
		 " /etc/xml/docbook"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "public"'
		f' "-//OASIS//ENTITIES DocBook XML Character Entities V{self.version}//EN"'
		f' "file://{PREFIX}/share/xml/docbook/xml-dtd-{self.version}/dbcentx.mod"'
		 " /etc/xml/docbook"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "public"'
		f' "-//OASIS//ENTITIES DocBook XML Additional General Entities V{self.version}//EN"'
		f' "file://{PREFIX}/share/xml/docbook/xml-dtd-{self.version}/dbgenent.mod"'
		 " /etc/xml/docbook"
	)

	self.cmd_run(
		 'xmlcatalog --noout --add "rewriteSystem"'
		f' "http://www.oasis-open.org/docbook/xml/{self.version}"'
		f' "file://{PREFIX}/share/xml/docbook/xml-dtd-{self.version}"'
		 " /etc/xml/docbook"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "rewriteURI"'
		f' "http://www.oasis-open.org/docbook/xml/{self.version}"'
		f' "file://{PREFIX}/share/xml/docbook/xml-dtd-{self.version}"'
		 " /etc/xml/docbook"
	)


	self.cmd_run(
		 "if [ ! -e /etc/xml/catalog ]; then"
		 " xmlcatalog --noout --create /etc/xml/catalog;"
		 " fi"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "delegatePublic"'
		 ' "-//OASIS//ENTITIES DocBook XML"'
		 ' "file:///etc/xml/docbook"'
		 " /etc/xml/catalog"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "delegatePublic"'
		 ' "-//OASIS//DTD DocBook XML"'
		 ' "file:///etc/xml/docbook"'
		 " /etc/xml/catalog"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "delegateSystem"'
		 ' "http://www.oasis-open.org/docbook/"'
		 ' "file:///etc/xml/docbook"'
		 " /etc/xml/catalog"
	)
	self.cmd_run(
		 'xmlcatalog --noout --add "delegateURI"'
		 ' "http://www.oasis-open.org/docbook/"'
		 ' "file:///etc/xml/docbook"'
		 " /etc/xml/catalog"
	)

def install(self):
	for ver in ["4.1.2", "4.2", "4.3", "4.4"]:
		self.cmd_run(
			'xmlcatalog --noout --add "public"'
			f' "-//OASIS//DTD DocBook XML V{ver}//EN"'
			f' "http://www.oasis-open.org/docbook/xml/{ver}/docbookx.dtd"'
			" /etc/xml/docbook"
		)
		self.cmd_run(
			'xmlcatalog --noout --add "rewriteSystem"'
			f' "http://www.oasis-open.org/docbook/xml/{ver}"'
			f' "file://{PREFIX}/share/xml/docbook/xml-dtd-{self.version}"'
			" /etc/xml/docbook"
		)
		self.cmd_run(
			'xmlcatalog --noout --add "rewriteURI"'
			f' "http://www.oasis-open.org/docbook/xml/{ver}"'
			f' "file://{PREFIX}/share/xml/docbook/xml-dtd-{self.version}"'
			" /etc/xml/docbook"
		)
		self.cmd_run(
			'xmlcatalog --noout --add "delegateSystem"'
			f' "http://www.oasis-open.org/docbook/xml/{ver}"'
			f' "file:///etc/xml/docbook"'
			" /etc/xml/catalog"
		)
		self.cmd_run(
			'xmlcatalog --noout --add "delegateURI"'
			f' "http://www.oasis-open.org/docbook/xml/{ver}"'
			f' "file:///etc/xml/docbook"'
			" /etc/xml/catalog"
		)