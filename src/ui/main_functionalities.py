"""
This module will contain class that implements base functionalities
"""
from abc import ABC

from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QHBoxLayout, QStackedWidget, QSizePolicy, QComboBox


def link_pages(button: QPushButton, page: QtWidgets.QWidget, stacked_widget: QStackedWidget):
    button.clicked.connect(lambda: stacked_widget.setCurrentWidget(page))


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
