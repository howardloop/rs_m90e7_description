from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
from launch.actions import TimerAction


def generate_launch_description():

    # ----------------------------------------------------------------
    # Get URDF via xacro
    # ----------------------------------------------------------------
    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            PathJoinSubstitution(
                [FindPackageShare("rs_m90e7_description"),
                 "urdf", "robot4.urdf.xacro"]
            ),
        ]
    )
    # ----------------------------------------------------------------
    rviz_config_file = PathJoinSubstitution(
        [FindPackageShare("rs_m90e7_description"), "rviz", "xarcro.rviz"]
    )
    # ----------------------------------------------------------------
    joint_state_publisher_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        name='joint_state_publisher_gui',
        parameters=[{'rate': 60.0}]
    )

    robot_description = {"robot_description": robot_description_content}
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="both",
        parameters=[robot_description,
                    {'publish_frequency': 60.0}],
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="log",
        arguments=["-d", rviz_config_file],
    )

    delay_start_node = TimerAction(
        period=2.0,  # 延遲2秒啟動
        actions=[
            rviz_node,
        ]
    )

    return LaunchDescription(
        [
            robot_state_publisher_node,
            joint_state_publisher_node,
            delay_start_node,
        ]
    )
