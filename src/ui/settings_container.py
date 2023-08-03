'''
This module create a menu container so user can navigate through the application.
Contains buttons like dashboard,entries etc
'''
from functools import partial

import main_functionalities
from PyQt6.QtCore import QSize, Qt, QPropertyAnimation, QEasingCurve, QObject
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QVBoxLayout, QFrame, QPushButton, QWidget, QHBoxLayout, QLabel
from PyQt6 import QtWidgets
from custom_widgets import QToggle
from global_variables import update_is_dark, GlobalVariables


class SettingsContainer:
    '''
    This class will implement a right settings menu widget with basic options for the user.
    This menu will be shown only when the user clicks on the settings button.
    Base implementation only allows simple settings.
    '''

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.dark_mode_toggle = QToggle(bg_color="#97acb8")
        self.dark_mode_toggle.stateChanged.connect(partial(self.dark_mode_toggled))

    def animate(self, object: QWidget, property_string, start_value: int, end_value: int, duration=500):
        self.animation = QPropertyAnimation(object, property_string)
        self.animation.setDuration(duration)
        self.animation.setStartValue(start_value)
        self.animation.setEndValue(end_value)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animation.start()

    def toggle_right_bar(self):
        # ANIMATION
        if self.right_menu_container.width() == 0:
            self.animate(self.right_menu_container, b"minimumWidth", 0, 200)
        elif self.right_menu_container.width() == 200:
            self.animate(self.right_menu_container, b"minimumWidth", 200, 0)


    def set_up(self):
        self.right_menu_container = QWidget()
        self.right_menu_container.setObjectName(u"rightMenuContainer")
        # set layout of main qwidget
        self.main_layout = QVBoxLayout()
        settings_label = QLabel("Ρυθμίσεις")
        settings_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        font = settings_label.font()
        font.setPointSize(15)
        settings_label.setFont(font)
        toggle_layout = QHBoxLayout()
        toggle_label = QLabel("Λειτουργία Νύχτας:")
        # self.main_layout.addWidget(settings_label)
        # Needs better styling because it looks terrible
        toggle_layout.addWidget(toggle_label)
        toggle_layout.addWidget(self.dark_mode_toggle)
        self.dark_mode_toggle.setChecked(GlobalVariables.is_dark)
        self.main_layout.addLayout(toggle_layout)
        toggle_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.right_menu_container.setLayout(self.main_layout)


        self.right_menu_container.setMinimumWidth(0)
        self.right_menu_container.setMaximumWidth(0)


    def get_widget(self):
        return self.right_menu_container

    def dark_mode_toggled(self, state):
        if state == 2:
            update_is_dark(True)
            self.parent.set_style_sheet(True)
        elif state == 0:
            update_is_dark(False)
            self.parent.set_style_sheet(False)
