import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():

    pub_etime = launch_ros.actions.Node(
            package='rbsys25_as2',
            executable='pub_etime',
            )
    sub_etime = launch_ros.actions.Node(
            package='rbsys25_as2',
            executable='sub_etime',
            output='screen'
            )

    return launch.LaunchDescription([pub_etime, sub_etime])
