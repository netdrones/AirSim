#!/bin/bash

echo "*** NetDrones Run Swarm Demo ***
Author: Deon Blaauw
Version: v1.0
********************************
"

pkill -x px4 || true

if [ $# -eq 0 ]; then
  echo "[WARNING] Please specify the number of drones to spawn e.g. ./netdrones_run_swarm_demo.sh 4 will spawn 4 drones.
  "
else

counter=1
while [ $counter -le $1 ]
do
  echo $counter
  gnome-terminal -x sh -c "./run_airsim_sitl.sh $counter; bash"
  ((counter++))
  done

echo All done

fi

