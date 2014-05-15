#! /usr/bin/env morseexec
# silgon <silgon3200@gmail.com>

""" Basic MORSE simulation scene for <test_2> environment

"""

from math import pi
from morse.builder import *
from test_2.builder.robots import Theman
from test_2.others.f_formations import *

poses=[] # x,y,theta

visAVis(poses,(4,4,pi/4),.6,()) 
visAVis(poses,(5,1,0),.6,()) 
LFormation(poses,(-3,2,pi/4),.6,()) 
circular4Formation(poses,(-3,-3,0),.6,()) 
circular4Formation(poses,(0,0,pi/4),.6,()) 
circular4Formation(poses,(7,7,0),.7,()) 
sideBySide(poses,(4,-3,0),.6,()) 
sideBySide(poses,(-7,-5,pi),.6,()) 

poses.append([0,-5,pi]) 
poses.append([-5,-5,pi/2]) 
poses.append([0,5,3*pi/2])



human=[]
motion=[]
pose=[]
for i in range(len(poses)):
    human.append(Theman())
    human[i].translate(poses[i][0], poses[i][1], 0.0)
    human[i].rotate(x = 0.0, y = 0.0, z = poses[i][2])
    motion.append(MotionXYW())
    motion[i].add_interface('ros',topic="human"+str(i)+"/motion")
    human[i].append(motion[i])
    pose.append(Pose())
    pose[i].add_stream('ros',topic="human"+str(i)+"/pose", frame_id=str(i+1000))
    human[i].append(pose[i])

# A PR2 robot to the scene
robot = BasePR2()
robot.add_interface('ros')
robot.translate(x=2.5, y=3.2, z=0.0)
robot.rotate(x=0.0, y=0.0, z=3.14)
# An odometry sensor to get odometry information
odometry = Odometry()
robot.append(odometry)
odometry.add_interface('ros', topic="/odom")
# Laser Scan
scan = Hokuyo()
scan.translate(x=0.275, z=0.252)
robot.append(scan)
scan.properties(Visible_arc = False)
scan.properties(laser_range = 30.0)
scan.properties(resolution = 1.0)
scan.properties(scan_window = 180.0)
scan.create_laser_arc()
scan.add_interface('ros', topic='/base_scan')
# Motion Controller
motion = MotionXYW()
robot.append(motion)
motion.add_interface('ros', topic='/cmd_vel')
motion.properties(ControlType = "Position")


# set 'fastmode' to True to switch to wireframe mode
env = Environment('../../environments/default.blend', fastmode = False)
# env.set_camera_location([10.0, -10.0, 10.0])
# env.set_camera_rotation([1.05, 0, 0.78])
env.place_camera([0, 0, 30])
env.aim_camera([0, 0, 0])

