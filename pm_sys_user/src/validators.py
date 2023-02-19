'''
In this module all the functionality of validators is taking place
'''
from PySide6 import QtGui


class MyValidator(QtGui.QValidator):
    """
        This function greets the person passed in as a parameter.

        :param name: The name of the person to greet
        :type name: str
        :return: A greeting for the person
        :rtype: str
        """
    def validate(self, input_string, pos):
        """
            This function greets the person passed in as a parameter.

            @param name: The name of the person to greet

            @return: A greeting for the person

            """
        try:
            value = int(input_string)
            if 0 <= value <= 100:
                return QtGui.QValidator.Acceptable, input_string, pos
            elif value < 0:
                return QtGui.QValidator.Intermediate, input_string, pos
            else:
                return QtGui.QValidator.Invalid, input_string, pos
        except ValueError:
            return QtGui.QValidator.Invalid, input_string, pos


