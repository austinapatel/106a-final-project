# Install script for directory: /home/eecs106a/Documents/hgfs/106a_final_project/ros_workspace/src/lab4/src/lab4_starter/ar_track_alvar/ar_track_alvar_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/eecs106a/Documents/hgfs/106a_final_project/ros_workspace/install")
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ar_track_alvar_msgs/msg" TYPE FILE FILES
    "/home/eecs106a/Documents/hgfs/106a_final_project/ros_workspace/src/lab4/src/lab4_starter/ar_track_alvar/ar_track_alvar_msgs/msg/AlvarMarker.msg"
    "/home/eecs106a/Documents/hgfs/106a_final_project/ros_workspace/src/lab4/src/lab4_starter/ar_track_alvar/ar_track_alvar_msgs/msg/AlvarMarkers.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ar_track_alvar_msgs/cmake" TYPE FILE FILES "/mnt/hgfs/106a_final_project/ros_workspace/build/lab4/src/lab4_starter/ar_track_alvar/ar_track_alvar_msgs/catkin_generated/installspace/ar_track_alvar_msgs-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/eecs106a/Documents/hgfs/106a_final_project/ros_workspace/devel/include/ar_track_alvar_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/eecs106a/Documents/hgfs/106a_final_project/ros_workspace/devel/share/roseus/ros/ar_track_alvar_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/eecs106a/Documents/hgfs/106a_final_project/ros_workspace/devel/share/common-lisp/ros/ar_track_alvar_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/eecs106a/Documents/hgfs/106a_final_project/ros_workspace/devel/share/gennodejs/ros/ar_track_alvar_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/eecs106a/Documents/hgfs/106a_final_project/ros_workspace/devel/lib/python2.7/dist-packages/ar_track_alvar_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/eecs106a/Documents/hgfs/106a_final_project/ros_workspace/devel/lib/python2.7/dist-packages/ar_track_alvar_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/mnt/hgfs/106a_final_project/ros_workspace/build/lab4/src/lab4_starter/ar_track_alvar/ar_track_alvar_msgs/catkin_generated/installspace/ar_track_alvar_msgs.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ar_track_alvar_msgs/cmake" TYPE FILE FILES "/mnt/hgfs/106a_final_project/ros_workspace/build/lab4/src/lab4_starter/ar_track_alvar/ar_track_alvar_msgs/catkin_generated/installspace/ar_track_alvar_msgs-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ar_track_alvar_msgs/cmake" TYPE FILE FILES
    "/mnt/hgfs/106a_final_project/ros_workspace/build/lab4/src/lab4_starter/ar_track_alvar/ar_track_alvar_msgs/catkin_generated/installspace/ar_track_alvar_msgsConfig.cmake"
    "/mnt/hgfs/106a_final_project/ros_workspace/build/lab4/src/lab4_starter/ar_track_alvar/ar_track_alvar_msgs/catkin_generated/installspace/ar_track_alvar_msgsConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ar_track_alvar_msgs" TYPE FILE FILES "/home/eecs106a/Documents/hgfs/106a_final_project/ros_workspace/src/lab4/src/lab4_starter/ar_track_alvar/ar_track_alvar_msgs/package.xml")
endif()

