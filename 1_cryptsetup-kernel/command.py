#!/usr/bin/env python3

from dot_mngr import *

def configure_kernel(self):
	self.kernel.config("MD", "y")
	self.kernel.config("BLK_DEV_DM", "y")
	self.kernel.config("DM_CRYPT", "y")
	self.kernel.config("CRYPTO", "y")
	self.kernel.config("CRYPTO_AES", "y")
	self.kernel.config("CRYPTO_TWOFISH", "y")
	self.kernel.config("CRYPTO_XTS", "y")
	self.kernel.config("CRYPTO_SHA256", "y")
	self.kernel.config("CRYPTO_USER_API_SKCIPHER", "y")
