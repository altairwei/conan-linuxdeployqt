import os, stat
from conans import ConanFile
from conans.client import tools

class LinuxdeployqtConan(ConanFile):
    name = "linuxdeployqt"
    # Conan: Valid names must contain at least 2 characters.
    version = "v6"
    license = "GPLv3", "LGPLv3"
    url = "https://github.com/altairwei/conan-linuxdeployqt.git"
    homepage = "https://github.com/probonopd/linuxdeployqt"
    settings = "os_build", "arch_build"
    build_policy = "missing"
    description = '''Makes Linux applications self-contained by copying in the
 libraries and plugins that the application uses, and optionally generates an
 AppImage. Can be used for Qt and other applications.'''
    generators = "cmake_find_package"

    def configure(self):
        if self.settings.os_build != "Linux":
            raise Exception("Only Linux supported for linuxdeployqt")
        if self.settings.arch_build != "x86_64":
            raise Exception("Only x86_64 supported for linuxdeployqt")

    def build(self):
        appimage_name = "linuxdeployqt-%s-x86_64.AppImage" % self.version[1]
        url = "https://github.com/probonopd/linuxdeployqt/releases/download/%s/%s" % (self.version[1], appimage_name)
        self.output.warn("Downloading %s: %s" % (appimage_name, url))
        tools.download(url, "linuxdeployqt")
        # Add execute permission
        st = os.stat('linuxdeployqt')
        os.chmod("linuxdeployqt", st.st_mode | stat.S_IEXEC)

    def package(self):
        self.copy("linuxdeployqt", dst="bin", keep_path=False)

    def package_info(self):
        self.output.info("Using linuxdeployqt-%s-x86_64.AppImage" % self.version[1])
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))