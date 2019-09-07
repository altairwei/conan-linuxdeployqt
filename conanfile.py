import os
from conans import ConanFile, CMake
from conans.client import tools


class LinuxdeployqtConan(ConanFile):
    name = "linuxdeployqt"
    # Conan: Valid names must contain at least 2 characters.
    version = "v6"
    license = "GPLv3", "LGPLv3"
    #TODO: add url to conan-linuxdeployqt
    url = ""
    settings = "os_build", "arch_build"
    build_policy = "missing"
    description = '''Makes Linux applications self-contained by copying in the
 libraries and plugins that the application uses, and optionally generates an
 AppImage. Can be used for Qt and other applications.'''
    requires = "qt/5.11.3@bincrafters/stable"
    generators = "cmake_find_package"
    _source_subfolder = "source_subfolder"

    def configure(self):
        if self.settings.os_build != "Linux":
            raise Exception("Only Linux supported for linuxdeployqt")

    def source(self):
        git = tools.Git(folder=self._source_subfolder)
        git.clone("https://github.com/probonopd/linuxdeployqt.git", self.version[1])

    def _configure_cmake(self):
        cmake = CMake(self)
        #TODO: set TRAVIS_BUILD_NUMBER
        cmake.configure(source_folder=self._source_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy("linuxdeployqt", src="tools/linuxdeployqt", dst="bin", keep_path=False)

    def deploy(self):
        self.copy("*", dst="bin", src="bin")

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))


        