# Install script for directory: /home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/src/move_grip

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/move_grip/msg" TYPE FILE FILES "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/src/move_grip/msg/MoveGripARMessage.msg")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/move_grip/cmake" TYPE FILE FILES "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/build/move_grip/catkin_generated/installspace/move_grip-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/devel/include/move_grip")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/devel/share/roseus/ros/move_grip")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/devel/share/common-lisp/ros/move_grip")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/devel/share/gennodejs/ros/move_grip")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/devel/lib/python2.7/dist-packages/move_grip")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/devel/lib/python2.7/dist-packages/move_grip")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/build/move_grip/catkin_generated/installspace/move_grip.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/move_grip/cmake" TYPE FILE FILES "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/build/move_grip/catkin_generated/installspace/move_grip-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/move_grip/cmake" TYPE FILE FILES
    "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/build/move_grip/catkin_generated/installspace/move_gripConfig.cmake"
    "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/build/move_grip/catkin_generated/installspace/move_gripConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/move_grip" TYPE FILE FILES "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/src/move_grip/package.xml")
endif()

