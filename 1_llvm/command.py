#!/usr/bin/env python3

from dot_mngr import *

def configure(self):
	download_package(self, "llvm-cmake")
	download_package(self, "llvm-third-party")
	download_package(self, "llvm-clang")
	download_package(self, "llvm-compiler-rt")

	self.chroot()

	llvm_cmake = conf.get_package("llvm-cmake")
	llvm_third_party = conf.get_package("llvm-third-party")
	llvm_clang = conf.get_package("llvm-clang")
	llvm_compiler_rt = conf.get_package("llvm-compiler-rt")

	llvm_cmake.prepare_archive(chroot=self.chrooted)
	llvm_third_party.prepare_archive(chroot=self.chrooted)
	llvm_clang.prepare_archive(chroot=self.chrooted)
	llvm_compiler_rt.prepare_archive(chroot=self.chrooted)

	self.cmd_run(
		f"tar -xf {self.chrooted_get_path(llvm_cmake.file_path, self.chrooted)}"
	)
	self.cmd_run(
		f"tar -xf {self.chrooted_get_path(llvm_third_party.file_path, self.chrooted)}"
	)
	self.cmd_run(
		 "sed '/LLVM_COMMON_CMAKE_UTILS/s@../cmake@llvm-cmake-19.src@'"
		 " -i CMakeLists.txt"
	)
	self.cmd_run(
		 "sed '/LLVM_THIRD_PARTY_DIR/s@../third-party@llvm-third-party-19.src@'"
		 " -i cmake/modules/HandleLLVMOptions.cmake"
	)
	self.cmd_run(
		f"tar -xf {self.chrooted_get_path(llvm_clang.file_path, self.chrooted)}"
		 " -C tools"
	)
	self.cmd_run(f"mv tools/{llvm_clang.archive_folder} tools/clang")
	self.cmd_run(
		f"tar -xf {self.chrooted_get_path(llvm_compiler_rt.file_path, self.chrooted)}"
		 " -C projects"
	)
	self.cmd_run(f"mv projects/{llvm_compiler_rt.archive_folder} projects/compiler-rt")
	self.cmd_run("grep -rl '#!.*python' | xargs sed -i '1s/python$/python3/'")
	self.cmd_run("sed 's/utility/tool/' -i utils/FileCheck/CMakeLists.txt")
	self.take_build()
	self.cmd_run(
		 "CC=gcc CXX=g++"
		 " cmake"
		f" -D CMAKE_INSTALL_PREFIX={PREFIX}"
		 " -D CMAKE_SKIP_INSTALL_RPATH=ON"
		 " -D LLVM_ENABLE_FFI=ON"
		 " -D CMAKE_BUILD_TYPE=Release"
		 " -D LLVM_BUILD_LLVM_DYLIB=ON"
		 " -D LLVM_LINK_LLVM_DYLIB=ON"
		 " -D LLVM_ENABLE_RTTI=ON"
		 ' -D LLVM_TARGETS_TO_BUILD="host;AMDGPU"'
		f" -D LLVM_BINUTILS_INCDIR={PREFIX}/include"
		 " -D LLVM_INCLUDE_BENCHMARKS=OFF"
		 " -D CLANG_DEFAULT_PIE_ON_LINUX=ON"
		 " -D CLANG_CONFIG_FILE_SYSTEM_DIR=/etc/clang"
		 " -W no-dev"
		 " -G Ninja"
	)

def compile(self):
	self.cmd_run("ninja")

def install(self):
	self.cmd_run("ninja install")
	self.cmd_run("mkdir -pv /etc/clang")
	self.cmd_run(
		 "for i in clang clang++; do"
		 " echo -fstack-protector-strong > /etc/clang/$i.cfg ;"
		 " done"
	)