#!/bin/bash

echo "*** NetDrones Run Swarm Demo ***

Author: Deon Blaauw
Version: v1.0"

pkill -x px4 || true

counter=1
while [ $counter -le $1 ]
do
echo $counter
gnome-terminal -x sh -c "./run_airsim_sitl.sh $counter; bash"
((counter++))
done
echo All done



