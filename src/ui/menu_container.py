'''
This module create a menu container so user can navigate through the application.
Contains buttons like dashboard,entries etc
'''
import main_functionalities
from PyQt6.QtCore import QSize, Qt, QPropertyAnimation, QEasingCurve, QObject
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QVBoxLayout, QFrame, QPushButton, QWidget
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
        self.animation = None
        # create the main widget

    def animate(self, object: QWidget, property_string, start_value: int, end_value: int, duration=500):
        """

        Args:
            object: The object whose property will be animated
            property_string: The property to be animated. Example use: b"minimumWidth"
            start_value: Starting value of animation
            end_value: Ending value of animation
            duration: Duration of animation in milliseconds

        Returns: void

        """
        self.animation = QPropertyAnimation(object, property_string)
        self.animation.setDuration(duration)
        self.animation.setStartValue(start_value)
        self.animation.setEndValue(end_value)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animation.start()

    def toggle_left_bar(self):
        """
        Toggles left menu bar

        Returns: void

        """
        if self.left_menu_container.width() == 100:
            self.animate(self.left_menu_container, b"minimumWidth", 100, 200)
        elif self.left_menu_container.width() == 200:
            self.animate(self.left_menu_container, b"minimumWidth", 200, 100)


    def set_up(self):
        self.left_menu_container = QWidget()
        self.left_menu_container.setObjectName(u"leftMenuContainer")
        # set layout of main qwidget
        self.main_layout = QVBoxLayout()
        self.left_menu_container.setLayout(self.main_layout)

        # create frames

        # frame 1
        frame_1 = main_functionalities.create_frame()

        # add corresponding buttons
        self.push_button_minimize = main_functionalities.add_button(frame_1.layout(), "align-justify.svg",
                                                                    text="  Απόκρυψη")

        # frame 2
        frame_2 = main_functionalities.create_frame()

        # add corresponding push buttons
        self.push_button_dashboard = main_functionalities.add_button(frame_2.layout(), "home.svg",
                                                                     text="  Αρχική Σελίδα", button_position='top')
        self.push_button_entries = main_functionalities.add_button(frame_2.layout(), "archive.svg",
                                                                   text="  Καταγραφές", button_position='middle')
        self.push_button_users = main_functionalities.add_button(frame_2.layout(), "users.svg", text="  Λογαριασμός",
                                                                 button_position='bottom')
        layout_frame = frame_2.layout()
        layout_frame.addSpacing(400)
        # frame 3
        frame_3 = main_functionalities.create_frame()

        # add corresponding push buttons
        self.push_button_help = main_functionalities.add_button(frame_3.layout(), "help-circle.svg", text="  Βοήθεια",
                                                                button_position='top')
        self.push_button_settings = main_functionalities.add_button(frame_3.layout(), "settings.svg",
                                                                    text="  Ρυθμίσεις", button_position='bottom')

        self.main_layout.addWidget(frame_1, alignment=Qt.AlignmentFlag.AlignTop)
        self.main_layout.addWidget(frame_2, alignment=Qt.AlignmentFlag.AlignTop)
        self.main_layout.addWidget(frame_3, alignment=Qt.AlignmentFlag.AlignBottom)

        self.left_menu_container.setMinimumWidth(100)
        self.left_menu_container.setMaximumWidth(100)

    def set_dark(self):
        """
        Sets everything to dark or bright mode based on global state of is_dark

        Returns: void
        """
        buttons = [self.push_button_help, self.push_button_settings, self.push_button_dashboard,
                   self.push_button_entries, self.push_button_users, self.push_button_minimize]
        for item in buttons:
            item.set_dark()

    def get_widget(self):
        return self.left_menu_container
