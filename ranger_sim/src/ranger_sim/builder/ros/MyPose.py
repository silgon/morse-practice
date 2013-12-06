from morse.middleware.ros import ROSPublisher
from std_msgs.msg import String


class MyPose(ROSPublisher):
    ros_class = String

    def default(self, ci='unused'):
        my_repr = []
        # my_repr.append("%.9f" % self.data['x'])
        # my_repr.append("%.9f" % self.data['y'])
        # my_repr.append("%.9f" % self.data['z'])
        self.data['y']=0
        my_repr.append(str(self.data['x']))
        my_repr.append(str(self.data['y']))
        my_repr.append(str(self.data['z']))
        msg = String(', '.join(my_repr))
        self.publish(msg)
