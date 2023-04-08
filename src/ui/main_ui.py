# main_window.py
import sys
import main_functionalities
from PyQt6.QtWidgets import QApplication, QSizePolicy, QWidget, QHBoxLayout
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt

from menu_container import MenuContainer
from main_container import MainContainer


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # to begin with : set application's size
        self.set_size()

        # create central widget and define its layout
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        cont_2 = MainContainer()
        cont_2.set_up()
        widg_2 = cont_2.get_widget()

        cont = MenuContainer()
        cont.set_up()
        widg = cont.get_widget()

        main_functionalities.link_pages(cont.push_button_entries, cont_2.page_entries, cont_2.main_menu_selection)
        main_functionalities.link_pages(cont.push_button_dashboard, cont_2.page_dashboard, cont_2.main_menu_selection)
        self.horizontalLayout.addWidget(cont.get_widget(), alignment=Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout.addWidget(cont_2.get_widget())
        self.setCentralWidget(self.centralwidget)
        self.set_style_sheet()
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
        self.setMinimumSize(550,450)

    def set_style_sheet(self):
        with open(r"C:\Users\billk\OneDrive\Documents\GitHub\pm_sys\cfg\styles.css", "r") as file:
            stylesheet = file.read()

        self.centralwidget.setStyleSheet(stylesheet)

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
