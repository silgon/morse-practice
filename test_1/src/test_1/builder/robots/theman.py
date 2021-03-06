from morse.builder import *
from morse.builder import Armature, Robot
from morse.builder.sensors import ArmaturePose

class Theman(Robot):
    """
    A template robot model for theman, with a motion controller and a pose sensor.
    """
    def __init__(self, name = None, debug = True):

        # theman.blend is located in the data/robots directory
        Robot.__init__(self, 'test_1/robots/theman.blend', name)
        self.properties(classpath = "test_1.robots.theman.Theman")
        self.suffix = self.name[-4:] if self.name[-4] == "." else ""
        try:
            self.armature = Armature("Armature" + self.suffix, "human_posture")
            # self.armature = Armature("Armature")
            self.append(self.armature)
            self.armature_pose = ArmaturePose() # armature_pose = joint states
            self.armature_pose.name="pose"
            self.armature.append(self.armature_pose)
            self.joint_state = CompoundSensor([self.armature_pose])
            self.append(self.joint_state)

        except KeyError:
            logger.error("Could not find the human armature! (I was looking " +\
                         "for an object called 'Armature' in the human" +\
                         " children). I won't be able to export the human pose" +\
                         " to any middleware.")


        ###################################
        # Actuators
        ###################################


        # (v,w) motion controller
        # Check here the other available actuators:
        # http://www.openrobots.org/morse/doc/stable/components_library.html#actuators

        # self.motion = MotionVW()
        # self.append(self.motion)

        # Optionally allow to move the robot with the keyboard
        if debug:
            keyboard = Keyboard()
            self.append(keyboard)

        ###################################
        # Sensors
        ###################################

        self.pose = Pose()
        self.append(self.pose)

    def add_interface(self, interface):
        if interface == "socket":
            self.joint_states.add_stream("socket")
            self.armature.add_service('socket')

        elif interface == "ros":

            # self.joint_states.add_stream("ros")

            # self.armature.add_service("ros")
            # self.armature.add_overlay("ros",
            #   "morse.middleware.ros.overlays.armatures.ArmatureController")
            self.armature_pose.add_stream("ros", 
                 "morse.middleware.ros.jointtrajectorycontrollers.JointTrajectoryControllerStatePublisher",
                 topic="/theman/state")
            self.armature_pose.add_overlay("ros",
              "morse.middleware.ros.overlays.armatures.ArmatureController",
              namespace = "/theman")


        elif interface == "pocolibs":
            self.armature.properties(classpath="morse.sensors.human_posture.HumanPosture")
            self.add_stream(interface)
