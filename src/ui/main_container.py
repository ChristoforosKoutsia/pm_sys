"""
This module implements the main container where all the data will be displayed
"""
from PyQt6.QtCore import QSize, Qt
from main_functionalities import BaseFunctionalities
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QVBoxLayout, QStackedWidget, QWidget, QSizePolicy


class Pages(BaseFunctionalities):
    '''
    This class will implement all the main menu pages
    '''

    def __init__(self):
        super().__init__()
        self.push_button_help = None
        self.push_button_settings = None

    def page_entries(self, page_widget: QWidget):
        # set layout
        page_layout = QVBoxLayout(page_widget)
        central_view_frame = self.create_frame('horizontal')

        # we want this frame to expand so the buttons are only on top!
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        central_view_frame.setSizePolicy(sizePolicy)
        push_buttons_selection_frame = self.create_frame("horizontal")

        # add corresponding push buttons
        self.push_button_help = self.add_button(push_buttons_selection_frame.layout(), text="help-circle.svg")
        self.push_button_settings = self.add_button(push_buttons_selection_frame.layout(), text="settings.svg")
        page_layout.addWidget(push_buttons_selection_frame,alignment=Qt.AlignmentFlag.AlignTop)

class MainContainer:
    """
    This class implements a stacked widget where all the different pages will appear
    """

    def __init__(self):
        super().__init__()
        self.push_button_settings = None
        self.push_button_help = None
        self.page_user = None
        self.page_entries = None
        self.page_settings = None
        self.page_help = None
        self.page_dashboard = None
        self.main_menu_selection = None
        self.main_layout = None
        self.main_container = None

    def set_up(self):
        # create instance of pages
        pages_obj = Pages()
        self.main_container = QtWidgets.QWidget()
        self.main_container.setObjectName("main_container")

        # set layout of main qwidget
        self.main_layout = QVBoxLayout(self.main_container)

        # create stacked widget
        self.main_menu_selection = QStackedWidget(self.main_container)

        # create corresponding pages
        self.page_dashboard = QWidget()
        self.page_entries = QWidget()
        pages_obj.page_entries(self.page_entries)

        self.page_user = QWidget()
        self.page_settings = QWidget()
        self.page_help = QWidget()

        # add pages
        self.main_menu_selection.addWidget(self.page_dashboard)
        self.main_menu_selection.addWidget(self.page_entries)
        self.main_menu_selection.addWidget(self.page_user)
        self.main_menu_selection.addWidget(self.page_settings)
        self.main_menu_selection.addWidget(self.page_help)

        # include in main_layout
        self.main_layout.addWidget(self.main_menu_selection)

    def get_widget(self):
        return self.main_container

    def page_entries(self, page_widget: QWidget):
        # set layout
        page_layout = QVBoxLayout(page_widget)
        central_view_frame = self.create_frame('horizontal')

        # we want this frame to expand so the buttons are only on top!
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        central_view_frame.setSizePolicy(sizePolicy)
        push_buttons_selection_frame = self.create_frame("horizontal")

        # add corresponding push buttons
        self.push_button_help = self.add_button(push_buttons_selection_frame.layout(), text="help-circle.svg")
        self.push_button_settings = self.add_button(push_buttons_selection_frame.layout(), text="settings.svg")

