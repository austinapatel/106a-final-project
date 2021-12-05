// Auto-generated. Do not edit!

// (in-package move_grip.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class MoveGripARMessage {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.object_robot_angle = null;
      this.wall_object_angle = null;
      this.timestamp = null;
    }
    else {
      if (initObj.hasOwnProperty('object_robot_angle')) {
        this.object_robot_angle = initObj.object_robot_angle
      }
      else {
        this.object_robot_angle = 0.0;
      }
      if (initObj.hasOwnProperty('wall_object_angle')) {
        this.wall_object_angle = initObj.wall_object_angle
      }
      else {
        this.wall_object_angle = 0.0;
      }
      if (initObj.hasOwnProperty('timestamp')) {
        this.timestamp = initObj.timestamp
      }
      else {
        this.timestamp = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MoveGripARMessage
    // Serialize message field [object_robot_angle]
    bufferOffset = _serializer.float32(obj.object_robot_angle, buffer, bufferOffset);
    // Serialize message field [wall_object_angle]
    bufferOffset = _serializer.float32(obj.wall_object_angle, buffer, bufferOffset);
    // Serialize message field [timestamp]
    bufferOffset = _serializer.float64(obj.timestamp, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MoveGripARMessage
    let len;
    let data = new MoveGripARMessage(null);
    // Deserialize message field [object_robot_angle]
    data.object_robot_angle = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [wall_object_angle]
    data.wall_object_angle = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [timestamp]
    data.timestamp = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'move_grip/MoveGripARMessage';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6d5beb0266670a57045cd6010a8b23d3';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 object_robot_angle
    float32 wall_object_angle
    float64 timestamp
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MoveGripARMessage(null);
    if (msg.object_robot_angle !== undefined) {
      resolved.object_robot_angle = msg.object_robot_angle;
    }
    else {
      resolved.object_robot_angle = 0.0
    }

    if (msg.wall_object_angle !== undefined) {
      resolved.wall_object_angle = msg.wall_object_angle;
    }
    else {
      resolved.wall_object_angle = 0.0
    }

    if (msg.timestamp !== undefined) {
      resolved.timestamp = msg.timestamp;
    }
    else {
      resolved.timestamp = 0.0
    }

    return resolved;
    }
};

module.exports = MoveGripARMessage;
