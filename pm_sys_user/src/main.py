import sys
import sys
import os

from pm_sys_core.src.data_objects import BaseDataObject
import data_storage
import user_objects
import data_storage
import json
from src.ui_py.try_1 import Ui_MainWindow
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
                               QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
                               QWidget, QTableWidget, QTableWidgetItem)

#
cat = user_objects.Expense.FIXED_EXPENSE_CATEGORIES[0]
typ = user_objects.Expense.TYPES_OF_CHARGE[1]
# i = user_objects.Income('JANUARY',500,12)
e = user_objects.Expense(cat, typ, 500, 6, 12)

# print(json.dumps(e.to_data_dict(), indent=4, sort_keys=True,ensure_ascii=False))
e.save()


# all = e.get()
# user = user_objects.User('ken1','pos')
# user2 = user_objects.User('ken1','pos')
# print(json.dumps(user.to_data_dict(), indent=4, sort_keys=True))
# user.save()
# user2.save()


class MainMenu(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainMenu, self).__init__()

        self.setupUi(self)

        self._link_pages()

        self._create_tables(user_objects.Expense, self.tableWidget_expenses)

        self._link_buttons()

        self._fill_combobox(self.type_of_chargecomboBox, user_objects.Expense.TYPES_OF_CHARGE)
        self._fill_combobox(self.fixed_expenses_box, user_objects.Expense.FIXED_EXPENSE_CATEGORIES)

    def _link_pages(self):
        # Main Menu linkage
        # entries linkage
        self.pushButton_entries.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.entries))
        self.pushButton_dashboard.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.dashboard))
        self.push_button_expenses.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_expenses_3))

    def _create_tables(self, input_class, table_name):
        '''

        Args:
            input_class: class that needs to be representes
            table_name: name of table as appears in ui (e.g tableWidget_expesnses)

        Returns:
            Nothing at all. Just creates the table in the ui
        '''
        # get all_objects from input class as a list
        all_objects = input_class.get()

        # flag that indicates that we entered for first time in columns for so we create once columns
        flag = False
        # convert them to list of dictionaries
        all_data_list = [i.to_data_dict() for i in all_objects]
        table_name.setRowCount(0)
        for idx_row, cont in enumerate(all_data_list):
            table_name.insertRow(idx_row)
            flag = False
            if idx_row == 0: flag = True
            for idx_col, item in enumerate(cont.items()):
                print(item)
                if flag:
                    table_name.insertColumn(idx_col)

                table_name.setItem(idx_row, idx_col, QTableWidgetItem(str(item[1])))

        # set column names
        headers = [i[0] for i in all_data_list[0].items()]
        print(headers)
        for h in headers:
            if h in user_objects.eng_2_greek.keys():
                headers = list(map(lambda x: x.replace(h, user_objects.eng_2_greek[h]), headers))
        table_name.setHorizontalHeaderLabels(headers)
        style = "::section {""background-color: lightblue; radius : 12px }"
        table_name.horizontalHeader().setStyleSheet(style)

    def _link_buttons(self):
        self.pushButton_newExpense.clicked.connect(lambda: self._hide_table(self.tableWidget_expenses))

        # self.pushButton_save_newExpense.clicked.connect(lambda : self.on_btn_clicked())

    def _hide_table(self, table_name):
        table_name.hide()

    def _show_table(self, table_name):
        table_name.show()

    def _fill_combobox(self, combobox, items):
        combobox.addItems(items)

    def on_btn_clicked(self):

        user_objects.Expense(self.fixed_expenses_box.currentText(),
                             self.type_of_chargecomboBox.currentText(),
                             int(self.textEdit_4.toPlainText()),
                             int(self.textEdit_6.toPlainText()),
                             int(self.textEdit_8.toPlainText()),
                             ).save()
        self._create_tables(user_objects.Expense, self.tableWidget_expenses)




#
# class UIIncomes  (QMainWindow, Ui_MainWindow)


app = QApplication()
window = MainMenu()
window.show()
sys.exit(app.exec())
