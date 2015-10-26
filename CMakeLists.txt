##############################################################################
# Cmake
##############################################################################

cmake_minimum_required(VERSION 2.8.3)
project(qglv_opengl)

##############################################################################
# Find Packages
##############################################################################

find_package(catkin
    REQUIRED
    COMPONENTS
        cmake_modules
        ecl_build
    )

find_package(Eigen REQUIRED)
find_package(OpenGL REQUIRED)
find_package(GLEW REQUIRED)  # Opengl3 stuff
find_package(sophus REQUIRED)

# be nice to get rid of this as we only use it for two things - 1) text
# rendering and 2) libqglviewer doesn't directly depend on it, but
# including some of the example program apis brings in this
# requirement...
find_package(GLUT REQUIRED)

##############################################################################
# Catkin
##############################################################################

# Because it does not set an xxxx_INCLUDE_DIRS...
set(OPENGL_INCLUDE_DIRS ${OPENGL_INCLUDE_DIR})
set(GLUT_INCLUDE_DIRS ${GLUT_INCLUDE_DIR})

catkin_package(
    INCLUDE_DIRS include
    LIBRARIES ${PROJECT_NAME} 
#    CATKIN_DEPENDS
    DEPENDS
        Eigen
        GLUT
        GLEW
        OPENGL
        sophus
    )


##############################################################################
# Project Configuration
##############################################################################

ecl_enable_cxx11_compiler()
add_definitions(${catkin_DEFINITIONS})
include_directories(
    include
    ${catkin_INCLUDE_DIRS}
    ${EIGEN_INCLUDE_DIRS}
    ${GLUT_INCLUDE_DIR}
    ${GLEW_INCLUDE_DIRS}
    ${OPENGL_INCLUDE_DIR}
    ${sophus_INCLUDE_DIRS}
)

##############################################################################
# Sources
##############################################################################

add_subdirectory(include)
add_subdirectory(src)

##############################################################################
# Installs
##############################################################################

#install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
