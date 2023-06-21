# SimulationGazeboCamera
ROS2 simulation of a camera using gazebo and rviz2

![alt text](https://github.com/DanaWentBananas/SimulationGazeboCamera/blob/main/camera_gazebo_simulation.png?raw=true)

![alt text](https://github.com/DanaWentBananas/SimulationGazeboCamera/blob/main/camera_gazebo_graph.png?raw=true)


# ROS2 Gazebo Simulation with a camera sensor

This repository contains code for a ROS2 Gazebo simulation using the Humble Hawksbill version on Ubuntu 22.04 Jammy Jellyfish. The simulation utilizes Gazebo as the simulator and rviz2 as the visualizer.

## Acknowledgment

This project was inspired by and based on the work of this repo [https://github.com/joshnewans/urdf_example]

## Prerequisites

- ROS2 Humble Hawksbill
- Ubuntu 22.04 Jammy Jellyfish
- Gazebo
- xacro

## Getting the code on your machine
 
1. Create a workspace inside home (~)
```
mkdir camera_simulation_ws
```

2. Go inside the ws and create a src folder
```
cd camera_simulation_ws
git clone https://github.com/DanaWentBananas/SimulationGazeboCamera.git
```

3. Change the folder name from SimulationGazeboCamera to src


4. Go back to the ws
```
cd ..
```
OR
```
cd path_to/map_ws
```

6. build it
```
colcon build
```

7. source !!
```
sudo vim ~/.bashrc
```
inside the file add these lines:
```
source /opt/ros/humble/setup.bash
source ~/camera_simulation_ws/install/setup.bash
source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash

```


## Running the Simulation

To run the simulation, follow the steps below:

# Launch the launch file:
```
ros2 launch launch_pkg demo_robot_gazebo.launch.py
```

