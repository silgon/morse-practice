#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <test_1> environment
"""

from morse.builder import *
from math import pi

# human 1
human1 = Human()
human1.translate(x = 0.0, y = 0.0, z = 0.0)
human1.rotate(x = 0.0, y = 0.0, z = pi)
human1.disable_keyboard_control()

# human 2
human2 = Human()
human2.translate(x = -1.0, y = -1.0, z = 0.0)
human2.rotate(x = 0.0, y = 0.0, z = pi/2)
human2.disable_keyboard_control()

# human 3
human3 = Human()
human3.translate(x = -2.0, y = 0.0, z = 0.0)
human3.rotate(x = 0.0, y = 0.0, z = 0)
human3.disable_keyboard_control()

# A PR2 robot to the scene
# pr2 = BasePR2()
pr2 = BarePR2()
# james.add_interface('ros')
pr2.translate(x=-1, y=4, z=0.0)
pr2.rotate(x = 0.0, y = 0.0, z = 3*pi/2)

# set 'fastmode' to True to switch to wireframe mode
# env = Environment('sandbox', fastmode = False)
env = Environment('../data/environment/envi.blend', fastmode = False)
env.place_camera([4, 5, 2])
env.aim_camera([1.25, 0, 2.2])

