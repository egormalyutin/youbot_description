#!/usr/bin/env python3

from launch import LaunchDescription
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    # Generate robot_description from xacro
    robot_description_path = PathJoinSubstitution(
        [FindPackageShare("youbot_description"), "robots", "youbot.urdf.xacro"]
    )

    robot_description = {
        "robot_description": ParameterValue(
            Command(["xacro ", robot_description_path]), value_type=str
        )
    }

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher",
        output="screen",
        parameters=[robot_description],
    )

    rviz2 = Node(
        package="rviz2",
        executable="rviz2",
    )

    joint_state_publisher_gui = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
    )

    static_tf_publisher = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        arguments=["0", "0", "0", "0", "0", "0", "world", "base_footprint"],
    )

    return LaunchDescription(
        [
            robot_state_publisher_node,
            rviz2,
            joint_state_publisher_gui,
            static_tf_publisher,
        ]
    )
