// Generated by gencpp from file move_grip/MoveGripARMessage.msg
// DO NOT EDIT!


#ifndef MOVE_GRIP_MESSAGE_MOVEGRIPARMESSAGE_H
#define MOVE_GRIP_MESSAGE_MOVEGRIPARMESSAGE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace move_grip
{
template <class ContainerAllocator>
struct MoveGripARMessage_
{
  typedef MoveGripARMessage_<ContainerAllocator> Type;

  MoveGripARMessage_()
    : object_robot_angle(0.0)
    , wall_object_angle(0.0)
    , timestamp(0.0)  {
    }
  MoveGripARMessage_(const ContainerAllocator& _alloc)
    : object_robot_angle(0.0)
    , wall_object_angle(0.0)
    , timestamp(0.0)  {
  (void)_alloc;
    }



   typedef float _object_robot_angle_type;
  _object_robot_angle_type object_robot_angle;

   typedef float _wall_object_angle_type;
  _wall_object_angle_type wall_object_angle;

   typedef double _timestamp_type;
  _timestamp_type timestamp;





  typedef boost::shared_ptr< ::move_grip::MoveGripARMessage_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::move_grip::MoveGripARMessage_<ContainerAllocator> const> ConstPtr;

}; // struct MoveGripARMessage_

typedef ::move_grip::MoveGripARMessage_<std::allocator<void> > MoveGripARMessage;

typedef boost::shared_ptr< ::move_grip::MoveGripARMessage > MoveGripARMessagePtr;
typedef boost::shared_ptr< ::move_grip::MoveGripARMessage const> MoveGripARMessageConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::move_grip::MoveGripARMessage_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::move_grip::MoveGripARMessage_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace move_grip

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'move_grip': ['/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/ros_workspace/src/move_grip/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::move_grip::MoveGripARMessage_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::move_grip::MoveGripARMessage_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::move_grip::MoveGripARMessage_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::move_grip::MoveGripARMessage_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::move_grip::MoveGripARMessage_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::move_grip::MoveGripARMessage_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::move_grip::MoveGripARMessage_<ContainerAllocator> >
{
  static const char* value()
  {
    return "6d5beb0266670a57045cd6010a8b23d3";
  }

  static const char* value(const ::move_grip::MoveGripARMessage_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x6d5beb0266670a57ULL;
  static const uint64_t static_value2 = 0x045cd6010a8b23d3ULL;
};

template<class ContainerAllocator>
struct DataType< ::move_grip::MoveGripARMessage_<ContainerAllocator> >
{
  static const char* value()
  {
    return "move_grip/MoveGripARMessage";
  }

  static const char* value(const ::move_grip::MoveGripARMessage_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::move_grip::MoveGripARMessage_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 object_robot_angle\n\
float32 wall_object_angle\n\
float64 timestamp\n\
";
  }

  static const char* value(const ::move_grip::MoveGripARMessage_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::move_grip::MoveGripARMessage_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.object_robot_angle);
      stream.next(m.wall_object_angle);
      stream.next(m.timestamp);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MoveGripARMessage_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::move_grip::MoveGripARMessage_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::move_grip::MoveGripARMessage_<ContainerAllocator>& v)
  {
    s << indent << "object_robot_angle: ";
    Printer<float>::stream(s, indent + "  ", v.object_robot_angle);
    s << indent << "wall_object_angle: ";
    Printer<float>::stream(s, indent + "  ", v.wall_object_angle);
    s << indent << "timestamp: ";
    Printer<double>::stream(s, indent + "  ", v.timestamp);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MOVE_GRIP_MESSAGE_MOVEGRIPARMESSAGE_H
