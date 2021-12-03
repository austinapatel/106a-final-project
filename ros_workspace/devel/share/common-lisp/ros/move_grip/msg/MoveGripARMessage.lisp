; Auto-generated. Do not edit!


(cl:in-package move_grip-msg)


;//! \htmlinclude MoveGripARMessage.msg.html

(cl:defclass <MoveGripARMessage> (roslisp-msg-protocol:ros-message)
  ((angle
    :reader angle
    :initarg :angle
    :type cl:float
    :initform 0.0)
   (timestamp
    :reader timestamp
    :initarg :timestamp
    :type cl:float
    :initform 0.0))
)

(cl:defclass MoveGripARMessage (<MoveGripARMessage>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MoveGripARMessage>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MoveGripARMessage)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name move_grip-msg:<MoveGripARMessage> is deprecated: use move_grip-msg:MoveGripARMessage instead.")))

(cl:ensure-generic-function 'angle-val :lambda-list '(m))
(cl:defmethod angle-val ((m <MoveGripARMessage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader move_grip-msg:angle-val is deprecated.  Use move_grip-msg:angle instead.")
  (angle m))

(cl:ensure-generic-function 'timestamp-val :lambda-list '(m))
(cl:defmethod timestamp-val ((m <MoveGripARMessage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader move_grip-msg:timestamp-val is deprecated.  Use move_grip-msg:timestamp instead.")
  (timestamp m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MoveGripARMessage>) ostream)
  "Serializes a message object of type '<MoveGripARMessage>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'timestamp))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MoveGripARMessage>) istream)
  "Deserializes a message object of type '<MoveGripARMessage>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angle) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'timestamp) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MoveGripARMessage>)))
  "Returns string type for a message object of type '<MoveGripARMessage>"
  "move_grip/MoveGripARMessage")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoveGripARMessage)))
  "Returns string type for a message object of type 'MoveGripARMessage"
  "move_grip/MoveGripARMessage")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MoveGripARMessage>)))
  "Returns md5sum for a message object of type '<MoveGripARMessage>"
  "0e56a3d762472e92f3187aa263e58fa6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MoveGripARMessage)))
  "Returns md5sum for a message object of type 'MoveGripARMessage"
  "0e56a3d762472e92f3187aa263e58fa6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MoveGripARMessage>)))
  "Returns full string definition for message of type '<MoveGripARMessage>"
  (cl:format cl:nil "float32 angle~%float64 timestamp~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MoveGripARMessage)))
  "Returns full string definition for message of type 'MoveGripARMessage"
  (cl:format cl:nil "float32 angle~%float64 timestamp~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MoveGripARMessage>))
  (cl:+ 0
     4
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MoveGripARMessage>))
  "Converts a ROS message object to a list"
  (cl:list 'MoveGripARMessage
    (cl:cons ':angle (angle msg))
    (cl:cons ':timestamp (timestamp msg))
))
