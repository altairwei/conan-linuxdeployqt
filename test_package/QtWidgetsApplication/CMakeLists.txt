project(QtWidgetsApplication)

set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

find_package(Qt5Core REQUIRED)
find_package(Qt5Gui REQUIRED)
find_package(Qt5Widgets REQUIRED)

include_directories(example 
    ${Qt5Core_INCLUDE_DIRS} 
    ${Qt5Gui_INCLUDE_DIRS} 
    ${Qt5Widgets_INCLUDE_DIRS}
)

qt5_wrap_ui(mainwindow.ui)

add_executable(QtWidgetsApplication main.cpp mainwindow.cpp mainwindow.h)
target_link_libraries(QtWidgetsApplication Qt5::Core Qt5::Gui Qt5::Widgets)