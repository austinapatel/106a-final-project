# 106a-final-project

## Setup
1) There is some weird issue with ROS packages not being able to be retrived. Solution: https://community.husarion.com/t/canopen-ros-package-getting-started/475
Pretty much run the following commands:
```
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt-key del 421C365BD9FF1F717815A3895523BAEEB01FA116
```

2) how to install ROS dependencies for a project: https://github.com/ros-industrial/robotiq/issues/164#issuecomment-529063441
- do this for "robotiq" ROS workspace

3) how to acutate gripper from ros: https://github.com/ros-industrial/robotiq/issues/164#issuecomment-529063441
- see "robotiq" folder for code that is referenced in the above link

