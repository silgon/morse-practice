#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <test_2> environment

Feel free to edit this template as you like!
"""

from math import pi
from morse.builder import *
from test_2.builder.robots import Theman


human = Theman()
human.translate(0.0, 0.0, 0.0)
human.rotate(x = 0.0, y = 0.0, z = pi)
motion = MotionXYW()
motion.add_interface('ros')
human.append(motion)
pose = Pose()
pose.add_stream('ros', frame_id='human_1')
human.append(pose)

human2 = Theman()
human2.translate(-1.0, -1.0, 0.0)
human2.rotate(x = 0.0, y = 0.0, z = pi/2)
motion2 = MotionXYW()
motion2.add_interface('ros')
human2.append(motion2)
pose2 = Pose()
pose2.add_stream('ros', frame_id='human_2')
human2.append(pose2)

human3 = Theman()
human3.translate(-2.0, 0.0, 0.0)
human3.rotate(x = 0.0, y = 0.0, z = 3*pi/2)
motion3 = MotionXYW()
motion3.add_interface('ros')
human3.append(motion3)
pose3 = Pose()
pose3.add_stream('ros', frame_id='human_3')
human3.append(pose3)


# set 'fastmode' to True to switch to wireframe mode
env = Environment('sandbox', fastmode = False)
env.set_camera_location([10.0, -10.0, 10.0])
env.set_camera_rotation([1.05, 0, 0.78])

