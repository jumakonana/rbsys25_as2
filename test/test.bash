#!/bin/bash

ng () {
	echo ${1}
	res=1
}

res=0

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 run rbsys25_as2 pub_etime 
timeout 10 ros2 run rbsys25_as2 sub_etime > /tmp/rbsys25_as2.log


cat /tmp/rbsys25_as2.log | 
grep '  0 : 5'

exit $res
