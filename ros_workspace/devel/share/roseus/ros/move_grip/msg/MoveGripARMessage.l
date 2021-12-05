;; Auto-generated. Do not edit!


(when (boundp 'move_grip::MoveGripARMessage)
  (if (not (find-package "MOVE_GRIP"))
    (make-package "MOVE_GRIP"))
  (shadow 'MoveGripARMessage (find-package "MOVE_GRIP")))
(unless (find-package "MOVE_GRIP::MOVEGRIPARMESSAGE")
  (make-package "MOVE_GRIP::MOVEGRIPARMESSAGE"))

(in-package "ROS")
;;//! \htmlinclude MoveGripARMessage.msg.html


(defclass move_grip::MoveGripARMessage
  :super ros::object
  :slots (_object_robot_angle _wall_object_angle _timestamp ))

(defmethod move_grip::MoveGripARMessage
  (:init
   (&key
    ((:object_robot_angle __object_robot_angle) 0.0)
    ((:wall_object_angle __wall_object_angle) 0.0)
    ((:timestamp __timestamp) 0.0)
    )
   (send-super :init)
   (setq _object_robot_angle (float __object_robot_angle))
   (setq _wall_object_angle (float __wall_object_angle))
   (setq _timestamp (float __timestamp))
   self)
  (:object_robot_angle
   (&optional __object_robot_angle)
   (if __object_robot_angle (setq _object_robot_angle __object_robot_angle)) _object_robot_angle)
  (:wall_object_angle
   (&optional __wall_object_angle)
   (if __wall_object_angle (setq _wall_object_angle __wall_object_angle)) _wall_object_angle)
  (:timestamp
   (&optional __timestamp)
   (if __timestamp (setq _timestamp __timestamp)) _timestamp)
  (:serialization-length
   ()
   (+
    ;; float32 _object_robot_angle
    4
    ;; float32 _wall_object_angle
    4
    ;; float64 _timestamp
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _object_robot_angle
       (sys::poke _object_robot_angle (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _wall_object_angle
       (sys::poke _wall_object_angle (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float64 _timestamp
       (sys::poke _timestamp (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _object_robot_angle
     (setq _object_robot_angle (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _wall_object_angle
     (setq _wall_object_angle (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float64 _timestamp
     (setq _timestamp (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get move_grip::MoveGripARMessage :md5sum-) "6d5beb0266670a57045cd6010a8b23d3")
(setf (get move_grip::MoveGripARMessage :datatype-) "move_grip/MoveGripARMessage")
(setf (get move_grip::MoveGripARMessage :definition-)
      "float32 object_robot_angle
float32 wall_object_angle
float64 timestamp

")



(provide :move_grip/MoveGripARMessage "6d5beb0266670a57045cd6010a8b23d3")


