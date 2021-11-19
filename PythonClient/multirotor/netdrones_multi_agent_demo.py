import setup_path 
import airsim
import cv2
import numpy as np
import os
import pprint
import tempfile

# Use below in settings.json with Blocks environment
"""
{
	"SeeDocsAt": "https://github.com/Microsoft/AirSim/blob/master/docs/settings.md",
	"SettingsVersion": 1.2,
	"SimMode": "Multirotor",
	"ClockSpeed": 1,
	
	"Vehicles": {
		"Drone1": {
		  "VehicleType": "SimpleFlight",
		  "X": 4, "Y": 0, "Z": -2
		},
		"Drone2": {
		  "VehicleType": "SimpleFlight",
		  "X": 8, "Y": 0, "Z": -2
		}

    }
}
"""

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True, "Drone1")
client.enableApiControl(True, "Drone2")
client.armDisarm(True, "Drone1")
client.armDisarm(True, "Drone2")


f1 = client.takeoffAsync(vehicle_name="Drone1")
f2 = client.takeoffAsync(vehicle_name="Drone2")
f1.join()
f2.join()


f1 = client.moveToPositionAsync(0, 1, -3.5, 5, vehicle_name="Drone1")
f2 = client.moveToPositionAsync(0, 2, -5.5, 5, vehicle_name="Drone2")
f1.join()
f2.join()



client.moveToPositionAsync(0.2,9.2,-3.0,1,vehicle_name="Drone1").join()
client.moveToPositionAsync(0.2,9.2,-5.0,1,vehicle_name="Drone2").join()

print( "Client List: ")
print(client.listVehicles())

z = -3.5
print("flying on path...")
result = client.moveOnPathAsync([airsim.Vector3r(125,0,z),
                                airsim.Vector3r(125,-130,z),
                                airsim.Vector3r(0,-130,z),
                                airsim.Vector3r(0,0,z)],
                        12, 120,
                        airsim.DrivetrainType.ForwardOnly, airsim.YawMode(False,0), 20, 1,vehicle_name="Drone1").join()

z = -4.5
print("flying on path...")
result = client.moveOnPathAsync([airsim.Vector3r(125,2,z),
                                airsim.Vector3r(124,-128,z),
                                airsim.Vector3r(1,-130,z),
                                airsim.Vector3r(0,0,z)],
                        12, 120,
                        airsim.DrivetrainType.ForwardOnly, airsim.YawMode(False,0), 20, 1,vehicle_name="Drone2").join()

z = -3.0
# drone will over-shoot so we bring it back to the start point before landing.
client.moveToPositionAsync(0,0,z,1,vehicle_name="Drone1").join()
client.moveToPositionAsync(0,0,z,1,vehicle_name="Drone2").join()

print("landing...")
client.landAsync(vehicle_name="Drone1").join()
client.landAsync(vehicle_name="Drone2").join()

print("disarming...")
client.armDisarm(False, vehicle_name="Drone1")
client.armDisarm(False, vehicle_name="Drone2")

client.enableApiControl(False, vehicle_name="Drone1")
client.enableApiControl(False, vehicle_name="Drone2")
print("done.")