"""
This module will contain class that implements base functionalities
"""
from abc import ABC
from functools import partial

from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize, Qt, QEasingCurve, QPropertyAnimation, QObject
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QHBoxLayout, QStackedWidget, QSizePolicy, QComboBox, \
    QLineEdit
from pm_sys_user.src import user_objects


def link_pages(button: QPushButton, page: QtWidgets.QWidget, stacked_widget: QStackedWidget):
    button.clicked.connect(lambda: stacked_widget.setCurrentWidget(page))

def link_test(button: QPushButton):
    button.clicked.connect(partial(print, "Hello world"))

def create_frame(layout='vertical', parent_frame=""):
    '''
    parent_frame : the parent frame of the new one
    '''
    if type(parent_frame) == QFrame or type(parent_frame) == QtWidgets.QWidget:
        frame = QFrame(parent_frame)
    else:
        frame = QFrame()
    frame.setFrameShape(QFrame.Shape.StyledPanel)
    frame.setFrameShadow(QFrame.Shadow.Plain)
    # set layout of frame_2

    if layout == 'vertical':
        layout_frame = QVBoxLayout(frame)
    else:
        layout_frame = QHBoxLayout(frame)
    return frame


def map_string_to_policy(key):
    mapping_table = {'Minimum': QSizePolicy.Policy.Minimum, 'Maximum': QSizePolicy.Policy.Maximum,
                     'Fixed': QSizePolicy.Policy.Fixed,
                     'Expanding': QSizePolicy.Policy.Expanding}

    return mapping_table[key]


def add_button(layout, input_icon='', alignment='', text="", horizontal_policy='', vertical_policy=''):
    '''
    Args:
        vertical_policy:
        horizontal_policy:
        text: text that will be displayed in the button
        alignment: alignment of the button in the given layout,
        layout: the layout that push_button will be imported
        input_icon: if push button have icon then the name of svg should be passed(e.g align-justify.svg)

    Returns:
        Created push button in given layout
    '''
    push_button = QPushButton()
    if input_icon:
        icon = QIcon()

        icon.addFile(f"../../ui/img/feather/{input_icon}")
        push_button.setIcon(icon)
        push_button.setIconSize(QSize(30, 30))
    push_button.setText(text)
    # layout.addWidget(push_button, alignment=Qt.AlignmentFlag.AlignLeft)
    layout.addWidget(push_button)
    push_button.setMaximumSize(167, 167)
    push_button.resize(50, 50)
    if horizontal_policy in ['Minimum', 'Maximum', 'Fixed', 'Expanding']:
        sizePolicy = QSizePolicy(map_string_to_policy(horizontal_policy), map_string_to_policy(horizontal_policy))
        push_button.setSizePolicy(sizePolicy)
    return push_button


def minimize_frame(frame: QFrame):
    frame.hide()


def expand_frame(frame: QFrame):
    frame.show()


def fill_combobox(combobox: QComboBox, items):
    combobox.addItems(items)


class ValidateInput:
    """
    Abstract class to use as template for input validation
    """

    def __init__(self,attribute_name,input_class, line_edit: QLineEdit):
        """
           Args:
               text: The given text from the user to be validated
               input_class: the class that will be set from the user
               line_edit: The Qt object of line edit to deal with (e.g change its color or whatever)
           """
        self.value = None
        print(type(input_class))
        self.input_class = input_class
        self.data_type = type(getattr(self.input_class,attribute_name))
        self.line_edit = line_edit
        self.attribute_name = attribute_name

    def input_validation(self,text):
        try:
            self.value = self.data_type(text)
            setattr(self.input_class, self.attribute_name, self.value)
            self.line_edit.setToolTip("")
            self.line_edit.setStyleSheet("")
        except ValueError as e:
            # If the input is invalid, show an error message and set the frame color to red
            self.line_edit.setStyleSheet("border: 2px solid red;")
            print(e)
            self.line_edit.setToolTip(str(e))


