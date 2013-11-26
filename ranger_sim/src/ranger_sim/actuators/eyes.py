import logging; logger = logging.getLogger("morse." + __name__)

import morse.core.actuator

from morse.core.services import service, async_service, interruptible
from morse.core import status
from morse.helpers.components import add_data, add_property
from morse.core import mathutils

class Eyes(morse.core.actuator.Actuator):
    """Write here the general documentation of your actuator.
    It will appear in the generated online documentation.
    """
    _name = "Eyes"
    _short_desc = ""

    # define here the data fields required by your actuator
    # format is: field name, initial value, type, description

    add_data('left', 0.1, 'float', 'Left eye rotation, in radians')
    add_data('right', -0.1, 'float', 'Right eye rotation, in radians')

    def __init__(self, obj, parent=None):
        logger.info("%s initialization" % obj.name)
        # Call the constructor of the parent class
        super(self.__class__, self).__init__(obj, parent)

        # Do here actuator specific initializations
        self.left_eye = parent.bge_object.children["left_eye"]
        self.right_eye = parent.bge_object.children["right_eye"]


        logger.info('Component initialized')

    def default_action(self):
        """ Main loop of the actuator.

        Implements the component behaviour
        """
        l_orientation = mathutils.Euler([self.local_data['left'], 0.0, 0.0])
        self.left_eye.orientation = l_orientation.to_matrix()

        r_orientation = mathutils.Euler([self.local_data['right'], 0.0, 0.0])
        self.right_eye.orientation = r_orientation.to_matrix()
        # implement here the behaviour of your actuator
