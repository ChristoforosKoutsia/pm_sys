# main_window.py
import os
import sys
import main_functionalities
from PyQt6.QtWidgets import QApplication, QSizePolicy, QWidget, QHBoxLayout, QMainWindow
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from functools import partial

from menu_container import MenuContainer
from main_container import MainContainer
from settings_container import SettingsContainer

from global_variables import GlobalVariables


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # to begin with : set application's size
        self.set_size()
        # update_is_dark(True)
        # create central widget and define its layout
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.cont_2 = MainContainer()
        self.cont_2.set_up()
        widg_2 = self.cont_2.get_widget()

        self.cont = MenuContainer()
        self.cont.set_up()
        widg = self.cont.get_widget()

        cont_settings = SettingsContainer(self)
        cont_settings.set_up()

        main_functionalities.link_pages(self.cont.push_button_entries, self.cont_2.page_entries, self.cont_2.main_menu_selection)
        main_functionalities.link_pages(self.cont.push_button_dashboard, self.cont_2.page_dashboard, self.cont_2.main_menu_selection)
        self.cont.push_button_minimize.clicked.connect(partial(self.cont.toggle_left_bar))
        self.cont.push_button_settings.clicked.connect(partial(cont_settings.toggle_right_bar))
        self.horizontalLayout.addWidget(self.cont.get_widget())
        self.horizontalLayout.addWidget(self.cont_2.get_widget())
        self.horizontalLayout.addWidget(cont_settings.get_widget())
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(self.centralwidget)
        self.set_style_sheet(GlobalVariables.is_dark)
        self.setWindowTitle("pm_sys")
        self.show()

    def set_size(self):
        '''
        This function just set the size of main window and the resize policy
        Returns: Nothing
        '''

        self.resize(1205, 794)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(550, 450)

    def set_style_sheet(self, is_dark):
        # Get the current working directory
        current_dir = os.getcwd()

        # Go two folders back
        parent_dir = os.path.dirname(os.path.dirname(current_dir))
        if is_dark:
            styles_dir = os.path.join(parent_dir, 'cfg', 'styles.css')
        else:
            styles_dir = os.path.join(parent_dir, 'cfg', 'styles_light.css')
        with open(styles_dir, "r") as file:
            stylesheet = file.read()
        self.cont_2.set_dark()
        self.cont.set_dark()
        self.centralwidget.setStyleSheet(stylesheet)


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
