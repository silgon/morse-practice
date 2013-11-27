#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <test_1> environment
"""

from morse.builder import *
from math import pi
################
# human 1
################
human1 = Human()
human1.translate(x = 0.0, y = 0.0, z = 0.0)
human1.rotate(x = 0.0, y = 0.0, z = pi)
human1.disable_keyboard_control()
motion1 = MotionVW()
human1.append(motion1)
motion1.add_stream('ros')
pose1 = Pose()
pose1.add_stream('ros')
human1.append(pose1)

################
# human 2
################
human2 = Human()
human2.translate(x = -1.0, y = -1.0, z = 0.0)
human2.rotate(x = 0.0, y = 0.0, z = pi/2)
human2.disable_keyboard_control()
motion2 = MotionVW()
human2.append(motion2)
motion2.add_stream('ros')
pose2 = Pose()
pose2.add_stream('ros')
human2.append(pose2)

################
# human 3
################
human3 = Human()
human3.translate(x = -2.0, y = 0.0, z = 0.0)
human3.rotate(x = 0.0, y = 0.0, z = 0)
human3.disable_keyboard_control()
motion3 = MotionVW()
human3.append(motion3)
motion3.add_stream('ros')
pose3 = Pose()
pose3.add_stream('ros')
human3.append(pose3)

############################
# A PR2 robot to the scene
############################
pr2 = BasePR2()
# pr2 = BarePR2()
pr2.add_interface('ros')
pr2.translate(x=-1, y=4, z=0.0)
pr2.rotate(x = 0.0, y = 0.0, z = 3*pi/2)
# An odometry sensor to get odometry information
odometry = Odometry()
pr2.append(odometry)
odometry.add_interface('ros', topic="/odom")

# Keyboard control
keyboard = Keyboard()
pr2.append(keyboard)

# Laser Scan
scan = Hokuyo()
scan.translate(x=0.275, z=0.252)
pr2.append(scan)
scan.properties(Visible_arc = False)
scan.properties(laser_range = 30.0)
scan.properties(resolution = 1.0)
scan.properties(scan_window = 180.0)
scan.create_laser_arc()

scan.add_interface('ros', topic='/base_scan')

# Motion Controller
motion = MotionXYW()
pr2.append(motion)
motion.add_interface('ros', topic='/cmd_vel')

# Kinect
kinect=Kinect()
kinect.add_stream('ros')
pr2.append(kinect)

# set 'fastmode' to True to switch to wireframe mode
# env = Environment('sandbox', fastmode = False)
env = Environment('../data/environment/envi.blend', fastmode = False)
env.place_camera([4, 5, 2])
env.aim_camera([1.25, 0, 2.2])

