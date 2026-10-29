import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command


def generate_launch_description():
    package_share = get_package_share_directory('lunabotics')
    model_file = os.path.join(package_share, 'model', 'robot_sim.xacro')
    bridge_parameters = os.path.join(
        package_share, 'parameters', 'bridge_parameters.yaml')

    robot_description = ParameterValue(
        Command(['xacro ', model_file]), value_type=str)

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('ros_gz_sim'),
                'launch',
                'gz_sim.launch.py',
            )
        ),
        launch_arguments={'gz_args': '-r empty.sdf'}.items(),
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[
            {
                'robot_description': robot_description,
                'use_sim_time': True,
            }
        ],
    )

    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-world', 'empty',
            '-name', 'lunabotics',
            '-topic', 'robot_description',
            '-z', '0.01',
        ],
        output='screen',
    )

    delayed_spawn = TimerAction(period=5.0, actions=[spawn_robot])

    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='ros_gz_bridge',
        parameters=[{'config_file': bridge_parameters}],
        output='screen',
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        delayed_spawn,
        bridge,
    ])
