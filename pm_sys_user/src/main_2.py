import sys

from PySide6 import QtCharts
from validators import MyValidator
import user_objects
from src.ui_py.mainwindow import Ui_MainWindow
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QMargins)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
                               QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
                               QWidget, QTableWidget, QTableWidgetItem, QFrame, QVBoxLayout, QHBoxLayout)

from PySide6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice
from functools import partial
from PySide6.QtCore import QResource


class MyChart(QChart):

    def __init__(self, datas, parent=None):
        super(MyChart, self).__init__(parent)
        self._datas = datas

        self.legend().hide()
        self.setAnimationOptions(QChart.SeriesAnimations)

        self.outer = QPieSeries()
        self.inner = QPieSeries()
        self.outer.setHoleSize(0.35)
        self.inner.setPieSize(0.35)
        self.inner.setHoleSize(0.3)

        self.set_outer_series()
        self.set_inner_series()

        self.addSeries(self.outer)
        self.addSeries(self.inner)

    def set_outer_series(self):
        slices = list()
        for data in self._datas:
            slice_ = QPieSlice(data.category, data.price)
            slice_.setLabelVisible()
            # slice_.setColor(data.primary_color)
            # slice_.setLabelBrush(data.primary_color)

            slices.append(slice_)
            self.outer.append(slice_)

        # label styling
        for slice_ in slices:
            color = 'black'
            # if slice_.percentage() > 0.1:
            #     slice_.setLabelPosition(QPieSlice.LabelInsideHorizontal)
            #     color = 'white'

            label = "<p align='center' style='color:{}'>{}<br>{}%</p>".format(
                color,
                slice_.label(),
                round(slice_.percentage() * 100, 2)
            )
            slice_.setLabel(label)
            slice_.hovered.connect(partial(self.explode, slice_))
            # slice_.setColor(data.secondary_color)
            # slice_.setBorderColor(data.secondary_color)

    def set_inner_series(self):
        for data in self._datas:
            slice_ = self.inner.append(data.category, data.price)

    def explode(self, slice_, is_hovered):
        if is_hovered:
            start = slice_.startAngle()
            end = slice_.startAngle() + slice_.angleSpan()
            self.inner.setPieStartAngle(end)
            self.inner.setPieEndAngle(start + 360)
        else:
            self.inner.setPieStartAngle(0)
            self.inner.setPieEndAngle(360)

        slice_.setExplodeDistanceFactor(0.1)
        slice_.setExploded(is_hovered)


def _minimize_frame(frame):
    frame.hide()


def _expand_frame(frame):
    frame.show()


def _fill_combobox(combobox, items):
    combobox.addItems(items)


def _link_pages_helper(pushbutton, stacked_widget, page):
    pushbutton.clicked.connect(lambda: stacked_widget.setCurrentWidget(page))


def _create_tables(input_class, table_name):
    '''

        Args:
            input_class: class that needs to be representes
            table_name: name of table as appears in ui (e.g tableWidget_expesnses)

        Returns:
            Nothing at all. Just creates the table in the ui
        '''
    # get all_objects from input class as a list
    all_objects = input_class.get()
    print(all_objects)
    # flag that indicates that we entered for first time in columns for so we create once columns
    flag = False
    # convert them to list of dictionaries
    all_data_list = [i.to_data_dict() for i in all_objects]
    # initializing key
    del_keys = ['oid', 'is_active', 'is_deleted']
    # Remove Key from Dictionary List
    # Using list comprehension + dictionary comprehension
    all_data_list = [{key: val for key, val in sub.items() if key not in del_keys} for sub in all_data_list]

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
    try:
        headers = [i[0] for i in all_data_list[0].items()]
        print(headers)
        for idx, h in enumerate(headers):
            headers[idx] = user_objects.eng_2_greek[h]
        table_name.setHorizontalHeaderLabels(headers)
        style = "::section {""background-color: lightblue; radius : 12px }"
        table_name.horizontalHeader().setStyleSheet(style)
        table_name.verticalHeader().setStyleSheet(style)
    except IndexError:
        print("do nothing")

class MainMenu(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainMenu, self).__init__()

        self.setupUi(self)
        # on startup hide expense add widget
        _minimize_frame(self.frame_add_expense)
        self._link_pages()

        # create and link entries page

        # firstly create expenses page
        # create tables
        _create_tables(user_objects.Expense, self.expenses_tableWidget)

        # link buttons
        self._link_expenses_buttons()

        # combobox
        self._fill_expenses_comboboxes()
        my_datas = user_objects.Expense.get()
        chart = MyChart(my_datas)
        chart.setTitle("Έξοδα")
        title = chart.title()

        chart.setTitleBrush(QBrush(Qt.white))
        chart.setTitleFont(QFont("Arial", 14))
        chart.setMargins(QMargins(0,0,0,150))
        chart.setBackgroundVisible(False)
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        layout = QHBoxLayout(self.page_dashboard)
        layout.addWidget(chart_view)

        _link_pages_helper(self.dashboard_pushButton, self.main_menu_selection, chart_view)

        #validators
        type = MyValidator()
        #self.lineEdit_expense_price.setValidator(type)
    def try_some_random_things(self):
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_11.clicked.connect(lambda: self.on_btn_click())

    def on_btn_click(self):
        print("I am here")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred,
            QSizePolicy.Policy.Preferred)

        self.frame_7.setSizePolicy(sizePolicy)

    def on_text_changed(self, text):
        validator = self.lineEdit_expense_price.validator()
        state = validator.validate(text, 0)[0]
        if state == QtGui.QValidator.Acceptable:
            color = 'green'
        elif state == QtGui.QValidator.Intermediate:
            color = 'orange'
        else:
            color = 'red'
        self.lineEdit_expense_price.setStyleSheet(f'border: 2px solid {color};')
    def _link_pages(self):
        # main menu linkage
        _link_pages_helper(self.dashboard_pushButton, self.main_menu_selection, self.page_dashboard)
        _link_pages_helper(self.entries_pushButton, self.main_menu_selection, self.page_entries)
        _link_pages_helper(self.account_pushButton, self.main_menu_selection, self.page_account)

        # entries linkage
        _link_pages_helper(self.incomes_pushButton, self.entries_stackwidget, self.page_incomes)
        _link_pages_helper(self.expenses_pushButton, self.entries_stackwidget, self.page_expenses)
        _link_pages_helper(self.employees_pushButton, self.entries_stackwidget, self.page_account)

    def _link_expenses_buttons(self):
        self.pushButton_minimize_form.clicked.connect(lambda: _minimize_frame(self.frame_add_expense))
        self.new_expense_pushButton.clicked.connect(lambda: _expand_frame(self.frame_add_expense))
        self.pushButton_save_expense.clicked.connect(lambda: self._expense_button_click())

    def _fill_expenses_comboboxes(self):
        _fill_combobox(self.comboBox_expense_category, user_objects.Expense.FIXED_EXPENSE_CATEGORIES)
        _fill_combobox(self.comboBox_expense_type, user_objects.Expense.TYPES_OF_CHARGE)

    def _set_get_expense_entry(self):
        '''
        create new expense object based on user input
        Returns: dictionary of this object
        '''
        new_expense_object = user_objects.Expense(self.comboBox_expense_category.currentText(),
                                                  self.comboBox_expense_type.currentText(),
                                                  int(self.lineEdit_expense_price.text()),
                                                  int(self.lineEdit_expense_non_taxable_price.text()),
                                                  int(self.lineEdit_expense_vat.text()),
                                                  )
        new_expense_object.save()
        return new_expense_object.to_data_dict()

    def _add_item_in_table(self, table, expense_dict):
        rowPosition = table.rowCount()
        colposition = self.expenses_tableWidget.columnCount()
        print(rowPosition)
        print(colposition)
        idx_row = table.rowCount()
        table.insertRow(idx_row)
        for idx_col, item in enumerate(expense_dict.items()):
            table.setItem(idx_row, idx_col, QTableWidgetItem(str(item[1])))

    def _expense_button_click(self):
        expense_dict = self._set_get_expense_entry()
        self._add_item_in_table(self.expenses_tableWidget, expense_dict)


app = QApplication()
window = MainMenu()

window.show()
sys.exit(app.exec())
