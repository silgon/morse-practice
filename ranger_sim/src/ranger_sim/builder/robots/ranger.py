from morse.builder import *
from ranger_sim.builder.actuators import Eyes

class Ranger(Robot):
    """
    A template robot model for ranger, with a motion controller and a pose sensor.
    """
    def __init__(self, name = None, debug = True):

        # ranger.blend is located in the data/robots directory
        Robot.__init__(self, 'ranger_sim/robots/ranger.blend', name)
        self.properties(classpath = "ranger_sim.robots.ranger.Ranger")

        ###################################
        # Actuators
        ###################################
        self.eyes = Eyes()
        self.append(self.eyes)
        # (v,w) motion controller
        # Check here the other available actuators:
        # http://www.openrobots.org/morse/doc/stable/components_library.html#actuators
        self.motion = MotionVW()
        self.append(self.motion)

        # Optionally allow to move the robot with the keyboard
        if debug:
            keyboard = Keyboard()
            self.append(keyboard)

        ###################################
        # Sensors
        ###################################

        self.pose = Pose()
        self.append(self.pose)

