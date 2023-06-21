import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

    package_name = "launch_pkg
    #add your world path here
    world_path = "path-to-world"

    demo_robot_rviz_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name), 'launch', 'demo_robot_rviz.launch.py'
        )])
    )

    #RUNNING GAZEBO

    #THIS WAY DID NOT WORK
    # gazebo = IncludeLaunchDescription(
    #         PythonLaunchDescriptionSource([os.path.join(
    #             get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
    #             launch_arguments={'extra_gazebo_args': '--ros-args --params-file ' + gazebo_params_file}.items()
    #         )

    run_gazebo = ExecuteProcess(
            cmd=['gazebo', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so', world_path],
            output='screen'
        )
    
    spawn_entity = Node(
            package="gazebo_ros",
            executable="spawn_entity.py",
            arguments=[
                '-topic','robot_description',
                '-entity','dana_bot'
                ],
            output='screen'
        )
    

    return LaunchDescription([
        demo_robot_rviz_launch,
        run_gazebo,
        spawn_entity
    ])
    


