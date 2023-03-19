'''
This module create a menu container so user can navigate through the application.
Contains buttons like dashboard,entries etc
'''
import main_functionalities
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QVBoxLayout, QFrame, QPushButton
from PyQt6 import QtWidgets


class MenuContainer:
    '''
    This class will implement a left menu widget with basic buttons.
    Implements the base navigation widget for the user.
    Implements 3 different frames :
    frame_1 : Contains a button to minimize the menu window
    frame_2 : Contains all the navigation buttons (e,g dashboard button, entries button etc.)
    frame_3 : Help buttons like settings and help
    '''

    def __init__(self):
        super().__init__()

        self.push_button_help = None
        self.push_button_settings = None
        self.push_button_dashboard = None
        self.push_button_entries = None
        self.push_button_users = None
        self.push_button_minimize = None
        self.main_layout = None
        self.left_menu_container = None
        # create the main widget

    def set_up(self):
        self.left_menu_container = QtWidgets.QWidget()
        self.left_menu_container.setObjectName(u"leftMenuContainer")
        # set layout of main qwidget
        self.main_layout = QVBoxLayout()
        self.left_menu_container.setLayout(self.main_layout)

        # create frames

        # frame 1
        frame_1 = main_functionalities.create_frame()

        # add corresponding buttons
        self.push_button_minimize = main_functionalities.add_button(frame_1.layout(), "align-justify.svg")

        # frame 2
        frame_2 = main_functionalities.create_frame()

        # add corresponding push buttons
        self.push_button_dashboard = main_functionalities.add_button(frame_2.layout(), "home.svg")
        self.push_button_entries = main_functionalities.add_button(frame_2.layout(), "archive.svg")
        self.push_button_users = main_functionalities.add_button(frame_2.layout(), "users.svg")
        layout_frame = frame_2.layout()
        layout_frame.addSpacing(400)
        # frame 3
        frame_3 = main_functionalities.create_frame()

        # add corresponding push buttons
        self.push_button_help = main_functionalities.add_button(frame_3.layout(), "help-circle.svg")
        self.push_button_settings = main_functionalities.add_button(frame_3.layout(), "settings.svg")

        self.main_layout.addWidget(frame_1, alignment=Qt.AlignmentFlag.AlignTop)
        self.main_layout.addWidget(frame_2, alignment=Qt.AlignmentFlag.AlignTop)
        self.main_layout.addWidget(frame_3, alignment=Qt.AlignmentFlag.AlignBottom)


    def get_widget(self):
        return self.left_menu_container
