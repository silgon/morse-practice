#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <ranger_sim> environment

Feel free to edit this template as you like!
"""

from morse.builder import *
from ranger_sim.builder.robots import Ranger
# from ranger_sim.builder.ros.MyPose import MyPose
# print (MyPose._type_name) 

# human=Human()
# human.translate(3,1,0)
# human.add_interface('ros')
# human.disable_keyboard_control()
# human.profile()

robot = Ranger()
robot.translate(1.0, 0.0, 0.0)

# arm = KukaLWR()
# robot.append(arm)
# arm.translate(z=0.9)
# arm.add_interface('ros')

motion = MotionVW()
robot.append(motion)
motion.add_stream('ros','ranger_sim.builder.ros.MyMotion')

keyboard = Keyboard()
robot.append(keyboard)
pose = Pose()
robot.append(pose)
pose.add_stream('ros', 'ranger_sim.builder.ros.MyPose')

robot.add_default_interface('socket')

env = Environment('sandbox', fastmode = False)
env.place_camera([10.0, -10.0, 10.0])
env.aim_camera([1.05, 0, 0.78])

