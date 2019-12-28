# Ardumower-1
lawn mower project - works outdoor and used for cutting grass in lawn.
This package performs outdoor navigation with GPS. It can navigate in lawn while avoiding obstacles. 
This repo is made to run on a Ardumower (Ardumower.de), NVIDIA Jetson Nano with IMU (AdaFruit), Android GPS, and Hokuyo URG-04LX-UG01 lidar.

This package uses a combination of the following Nodes:

	- ekf_localization to fuse odometry data with IMU and GPS data or Just Odometry with IMU.

	- navsat_transform to convert GPS data to odometry and to convert latitude and longitude points to the robot's odometry coordinate system.
	
	- move_base to navigate to the goals while avoiding obstacles. (goals can also be set using recorded waypoints but in this case goal navigation is poor due to error in GPS data.)
