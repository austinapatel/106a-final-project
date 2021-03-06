# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "move_grip: 1 messages, 0 services")

set(MSG_I_FLAGS "-Imove_grip:/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/src/move_grip/msg;-Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(move_grip_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/src/move_grip/msg/MoveGripARMessage.msg" NAME_WE)
add_custom_target(_move_grip_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "move_grip" "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/src/move_grip/msg/MoveGripARMessage.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(move_grip
  "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/src/move_grip/msg/MoveGripARMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/move_grip
)

### Generating Services

### Generating Module File
_generate_module_cpp(move_grip
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/move_grip
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(move_grip_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(move_grip_generate_messages move_grip_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/src/move_grip/msg/MoveGripARMessage.msg" NAME_WE)
add_dependencies(move_grip_generate_messages_cpp _move_grip_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(move_grip_gencpp)
add_dependencies(move_grip_gencpp move_grip_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS move_grip_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(move_grip
  "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/src/move_grip/msg/MoveGripARMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/move_grip
)

### Generating Services

### Generating Module File
_generate_module_eus(move_grip
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/move_grip
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(move_grip_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(move_grip_generate_messages move_grip_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/src/move_grip/msg/MoveGripARMessage.msg" NAME_WE)
add_dependencies(move_grip_generate_messages_eus _move_grip_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(move_grip_geneus)
add_dependencies(move_grip_geneus move_grip_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS move_grip_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(move_grip
  "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/src/move_grip/msg/MoveGripARMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/move_grip
)

### Generating Services

### Generating Module File
_generate_module_lisp(move_grip
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/move_grip
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(move_grip_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(move_grip_generate_messages move_grip_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/src/move_grip/msg/MoveGripARMessage.msg" NAME_WE)
add_dependencies(move_grip_generate_messages_lisp _move_grip_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(move_grip_genlisp)
add_dependencies(move_grip_genlisp move_grip_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS move_grip_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(move_grip
  "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/src/move_grip/msg/MoveGripARMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/move_grip
)

### Generating Services

### Generating Module File
_generate_module_nodejs(move_grip
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/move_grip
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(move_grip_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(move_grip_generate_messages move_grip_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/src/move_grip/msg/MoveGripARMessage.msg" NAME_WE)
add_dependencies(move_grip_generate_messages_nodejs _move_grip_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(move_grip_gennodejs)
add_dependencies(move_grip_gennodejs move_grip_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS move_grip_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(move_grip
  "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/src/move_grip/msg/MoveGripARMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/move_grip
)

### Generating Services

### Generating Module File
_generate_module_py(move_grip
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/move_grip
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(move_grip_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(move_grip_generate_messages move_grip_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/src/move_grip/msg/MoveGripARMessage.msg" NAME_WE)
add_dependencies(move_grip_generate_messages_py _move_grip_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(move_grip_genpy)
add_dependencies(move_grip_genpy move_grip_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS move_grip_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/move_grip)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/move_grip
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(move_grip_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/move_grip)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/move_grip
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(move_grip_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/move_grip)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/move_grip
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(move_grip_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/move_grip)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/move_grip
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(move_grip_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/move_grip)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/move_grip\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/move_grip
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(move_grip_generate_messages_py geometry_msgs_generate_messages_py)
endif()
