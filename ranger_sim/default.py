#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <ranger_sim> environment

Feel free to edit this template as you like!
"""

from morse.builder import *
from ranger_sim.builder.robots import Ranger

robot = Ranger()
robot.translate(1.0, 0.0, 0.0)

motion = MotionVW()
robot.append(motion)

keyboard = Keyboard()
robot.append(keyboard)
pose = Pose()
robot.append(pose)

robot.add_default_interface('socket')

env = Environment('sandbox', fastmode = False)
env.place_camera([10.0, -10.0, 10.0])
env.aim_camera([1.05, 0, 0.78])

