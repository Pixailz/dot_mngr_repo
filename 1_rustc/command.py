#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	self.chroot()
	self.cmd_run(f"mkdir -pv /opt/rustc-{self.version}")
	self.cmd_run(f"ln -svfn rustc-{self.version} /opt/rustc")
	self.cmd_run(
		 "cat > config.toml << EOF\n"
		 '# see config.toml.example for more possible options\n'
		 '# See the 8.4 book for an old example using shipped LLVM\n'
		 '# e.g. if not installing clang, or using a version before 13.0\n'
		 '\n'
		 '# Tell x.py the editors have reviewed the content of this file\n'
		 '# and updated it to follow the major changes of the building system,\n'
		 '# so x.py will not warn us to do such a review.\n'
		 'change-id = 127866\n'
		 '\n'
		 '[llvm]\n'
		 '# by default, rust will build for a myriad of architectures\n'
		 'targets = "X86"\n'
		 '\n'
		 '# When using system llvm prefer shared libraries\n'
		 'link-shared = true\n'
		 '\n'
		 '[build]\n'
		 '# omit docs to save time and space (default is to build them)\n'
		 'docs = false\n'
		 '\n'
		 '# install extended tools: cargo, clippy, etc\n'
		 'extended = true\n'
		 '\n'
		 '# Do not query new versions of dependencies online.\n'
		 'locked-deps = true\n'
		 '\n'
		 '# Specify which extended tools (those from the default install).\n'
		 'tools = ["cargo", "clippy", "rustdoc", "rustfmt"]\n'
		 '\n'
		 '# Use the source code shipped in the tarball for the dependencies.\n'
		 '# The combination of this and the "locked-deps" entry avoids downloading\n'
		 '# many crates from Internet, and makes the Rustc build more stable.\n'
		 'vendor = true\n'
		 '\n'
		 '[install]\n'
		f'prefix = "/opt/rustc-{self.version}"\n'
		f'docdir = "share/doc/rustc-{self.version}"\n'
		 '\n'
		 '[rust]\n'
		 'channel = "stable"\n'
		 'description = "for BLFS"\n'
		 '\n'
		 '# Enable the same optimizations as the official upstream build.\n'
		 'lto = "thin"\n'
		 'codegen-units = 1\n'
		 '\n'
		 '[target.x86_64-unknown-linux-gnu]\n'
		 '# NB the output of llvm-config (i.e. help options) may be\n'
		 '# dumped to the screen when config.toml is parsed.\n'
		f'llvm-config = "{PREFIX}/bin/llvm-config"\n'
		 '\n'
		 '[target.i686-unknown-linux-gnu]\n'
		 '# NB the output of llvm-config (i.e. help options) may be\n'
		 '# dumped to the screen when config.toml is parsed.\n'
		f'llvm-config = "{PREFIX}/bin/llvm-config"\n'
		 'EOF'
	)
	self.cmd_run("sed '/MirOpt/d' -i src/bootstrap/src/core/builder.rs")
	self.cmd_run(
		 "sed 's/!path.ends_with(\"cargo\")/true/'"
		 " -i src/bootstrap/src/core/build_steps/tool.rs"
	)
	self.cmd_run(
		 "sed 's/^.*build_wasm.*$/#[allow(unreachable_code)]&return false;/'"
		 " -i src/bootstrap/src/lib.rs"
	)
	self.cmd_run(
		 "sed '/CondBitmap/,/^}/s/LLVM_VERSION.*/& \&\& LLVM_VERSION_LT(19, 0)/'"
		 " -i compiler/rustc_llvm/llvm-wrapper/RustWrapper.cpp"
	)
	self.cmd_run("rm -v tests/coverage/mcdc/{cond*,if,inline*,nest*,non_*}.rs")

def compile(self):
	libssh2 = "0"
	sqlite = "0"
	if conf.is_installed("1_libssh2", False):
		libssh2 = "1"
	if conf.is_installed("1_sqlite", False):
		sqlite = "1"
	self.cmd_run(
		 "export"
		f" LIBSSH2_SYS_USE_PKG_CONFIG={libssh2}"
		f" LIBSQLITE3_SYS_USE_PKG_CONFIG={sqlite}"
		 " &&"
		 "   python3 x.py build"
		 " &&"
		 "   python3 x.py install rustc std"
		 " &&"
		 "   python3 x.py install --stage=1 cargo clippy rustfmt"
	)

def install(self):
	self.cmd_run(
		f"rm -fv /opt/rustc-{self.version}/share/doc/rustc-{self.version}/*.old"
	)
	self.cmd_run(
		 "install -vm644 README.md"
		f" /opt/rustc-{self.version}/share/doc/rustc-{self.version}"
	)
	self.cmd_run(f"install -vdm755 {PREFIX}/share/zsh/site-functions")
	self.cmd_run(
		 "ln -sfv /opt/rustc/share/zsh/site-functions/_cargo"
		f" {PREFIX}/share/zsh/site-functions"
	)
	self.cmd_run(
		 "mv -v /etc/bash_completion.d/cargo"
		f" {PREFIX}/share/bash-completion/completions"
	)