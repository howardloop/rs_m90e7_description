import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    rs_m90e7_description_path = get_package_share_directory('rs_m90e7_description')
    rviz_file = os.path.join(rs_m90e7_description_path, 'rviz', 'urdf.rviz')    
    urdf_file = os.path.join(rs_m90e7_description_path, 'urdf', 'rs_m90e7_description.urdf')

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
        arguments=[urdf_file],
        parameters=[{'publish_frequency': 100.0}]
    )

    rviz2_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_file]
    )

    return LaunchDescription([
        joint_state_publisher_gui_node,
        robot_state_publisher_node,
        rviz2_node
    ])