from morse.builder import *

class Theman(Robot):
    """
    A template robot model for theman, with a motion controller and a pose sensor.
    """
    def __init__(self, name = None, debug = True):

        # theman.blend is located in the data/robots directory
        Robot.__init__(self, 'test_3/robots/theman.blend', name)
        self.properties(classpath = "test_3.robots.theman.Theman")

        ###################################
        # Actuators
        ###################################


        # (v,w) motion controller
        # Check here the other available actuators:
        # http://www.openrobots.org/morse/doc/stable/components_library.html#actuators
        # self.motion = MotionVW()
        # self.append(self.motion)

        # Optionally allow to move the robot with the keyboard
        # if debug:
        #     keyboard = Keyboard()
        #     keyboard.properties(ControlType = 'Position')
        #     self.append(keyboard)

        ###################################
        # Sensors
        ###################################

        # self.pose = Pose()
        # self.append(self.pose)

