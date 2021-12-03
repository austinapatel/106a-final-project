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
  :slots (_angle _timestamp ))

(defmethod move_grip::MoveGripARMessage
  (:init
   (&key
    ((:angle __angle) 0.0)
    ((:timestamp __timestamp) 0.0)
    )
   (send-super :init)
   (setq _angle (float __angle))
   (setq _timestamp (float __timestamp))
   self)
  (:angle
   (&optional __angle)
   (if __angle (setq _angle __angle)) _angle)
  (:timestamp
   (&optional __timestamp)
   (if __timestamp (setq _timestamp __timestamp)) _timestamp)
  (:serialization-length
   ()
   (+
    ;; float32 _angle
    4
    ;; float64 _timestamp
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _angle
       (sys::poke _angle (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float64 _timestamp
       (sys::poke _timestamp (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _angle
     (setq _angle (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float64 _timestamp
     (setq _timestamp (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get move_grip::MoveGripARMessage :md5sum-) "0e56a3d762472e92f3187aa263e58fa6")
(setf (get move_grip::MoveGripARMessage :datatype-) "move_grip/MoveGripARMessage")
(setf (get move_grip::MoveGripARMessage :definition-)
      "float32 angle
float64 timestamp
")



(provide :move_grip/MoveGripARMessage "0e56a3d762472e92f3187aa263e58fa6")


