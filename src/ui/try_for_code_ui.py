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

        main_functionalities.link_pages(cont.push_button_entries,cont_2.page_entries,cont_2.main_menu_selection)
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

    def set_style_sheet(self):
        with open(r"C:\Users\billk\OneDrive\Documents\GitHub\pm_sys\cfg\styles.css", "r") as file:
            stylesheet = file.read()

        self.centralwidget.setStyleSheet(stylesheet)


class ExpensesStack(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 250, 250)
        self.setWindowTitle("QLabel Example")
        label = QtWidgets.QLabel("Hello World!", self)
        label.move(100, 100)


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
