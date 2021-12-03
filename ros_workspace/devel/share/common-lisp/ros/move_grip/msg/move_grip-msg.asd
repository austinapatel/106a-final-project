
(cl:in-package :asdf)

(defsystem "move_grip-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "MoveGripARMessage" :depends-on ("_package_MoveGripARMessage"))
    (:file "_package_MoveGripARMessage" :depends-on ("_package"))
  ))