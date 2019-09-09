import os
from conans import ConanFile, CMake

class QtWidgetsApplicationTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "linuxdeployqt/v6", "qt/5.11.3@bincrafters/stable"
    generators = "cmake_find_package"
    _source_subfolder = "QtWidgetsApplication"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self._source_subfolder)
        cmake.build()

    def test(self):
        executable = os.path.join(self.build_folder, "QtWidgetsApplication")
        self.run("linuxdeployqt %s -unsupported-allow-new-glibc" % executable, run_environment=True)
        self.run(executable)
        return