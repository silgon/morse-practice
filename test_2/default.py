#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <test_2> environment

"""

from math import pi
from morse.builder import *
from test_2.builder.robots import Theman


poses=[] # x,y,theta
poses.append([0,0,pi]) # human 1
poses.append([-1,-1,pi/2]) # human 2
poses.append([-2,0,3*pi/2]) # human 3
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
    pose[i].add_stream('ros',topic="human"+str(i)+"/pose", frame_id='human_'+str(i))
    human[i].append(pose[i])


# set 'fastmode' to True to switch to wireframe mode
env = Environment('../data/environment/envi.blend', fastmode = False)
env.set_camera_location([10.0, -10.0, 10.0])
env.set_camera_rotation([1.05, 0, 0.78])

