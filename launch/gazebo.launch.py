from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from ament_index_python.packages import get_package_prefix
from launch.actions import SetEnvironmentVariable
import os

def generate_launch_description():

    rviz_file = PathJoinSubstitution(
        [FindPackageShare("rs_m90e7_description"), "rviz", "urdf.rviz"])
    urdf_file = PathJoinSubstitution(
        [FindPackageShare("rs_m90e7_description"), "urdf", "rs_m90e7.urdf"])

    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        parameters=[{'rate': 60.0}]
    )

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output="both",
        arguments=[urdf_file],
        parameters=[{'publish_frequency': 100.0}]
    )

    rviz2_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output="both",
        arguments=['-d', rviz_file]
    )

    gazebo_env = SetEnvironmentVariable(
        "GAZEBO_MODEL_PATH",
        os.path.join(get_package_prefix("rs_m90e7_description"), "share"),
    )
    
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                PathJoinSubstitution(
                    [FindPackageShare("gazebo_ros"), "launch", "gazebo.launch.py"]
                )
            ]
        )
    )

    spawn_entity = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-file", urdf_file, "-entity", "arm"],
        output="screen",
    )

    return LaunchDescription(
        [
            joint_state_publisher_gui_node,
            robot_state_publisher_node,
            rviz2_node,
            gazebo_env,
            gazebo,
            spawn_entity,
        ]
    )
