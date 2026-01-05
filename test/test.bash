#!/bin/bash

ng () {
	echo ${1}に問題あり
}

res=0

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 70 ros2 launch rbsys25_as2 etime.launch.py > /tmp/rbsys25_as2.log

out=$(cat /tmp/rbsys25_as2.log | grep '  0 : 5')
[ "$?" = 0 ] || ng "$LINENO"

out=$(cat /tmp/rbsys25_as2.log | grep '  1 : 0')
[ "$?" = 0 ] || ng "$LINENO"

out=$(cat /tmp/rbsys25_as2.log | grep '  0 : 60')
[ "$?" = 1 ] || ng "$LINENO"

exit $res

