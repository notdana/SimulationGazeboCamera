import os
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import LaunchConfiguration, Command
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch_ros.actions import Node
import xacro

def generate_launch_description():

    urdf_pkg = 'descriptions_pkg'
    urdf_subpath = "descriptions/demo_robot.urdf.xacro"

    #process the file using xacro
    xacro_file = os.path.join(get_package_share_directory(urdf_pkg),urdf_subpath)
    robot_description = xacro.process_file(xacro_file).toxml()

    #robot_state_publisher node
    robot_state_pub_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[
            {'robot_description': robot_description,
             'use_sim_time': False
            }
        ]
    )

    #rviz node
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        output="screen"
    )

    #joint node
    joint_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        output="screen"
    )

    #RUN NODES
    return LaunchDescription([
        robot_state_pub_node,
        rviz_node,
        #joint_node
    ])

