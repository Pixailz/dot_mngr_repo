#!/usr/bin/env python3

from dot_mngr import *

def configure_kernel(self):
	self.kernel.config("NAMESPACES", "y")
	self.kernel.config("USER_NS", "y")
