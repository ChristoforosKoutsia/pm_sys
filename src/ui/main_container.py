"""
This module implements the main container where all the data will be displayed
"""
from abc import ABC, abstractmethod
from functools import partial

from PyQt6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice
from PyQt6.QtCore import Qt, QMargins
from PyQt6.QtGui import QPainter, QBrush, QFont

from pm_sys_user.src import user_objects

from main_functionalities import create_frame, add_button
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QVBoxLayout, QStackedWidget, QWidget, QSizePolicy, QTableWidgetItem, QTableWidget, \
    QComboBox, QLabel, QLineEdit, QFrame, QHBoxLayout

from src.ui import main_functionalities


class BaseEntriesDesign(ABC):
    """
    This class will implement the base design of the entries.
    Since all entries (expenses ,incomes ,employees etc) will have almost the same widgets it is a good idea
    to have an abstract class for them
    """

    def __init__(self):

        self.frame_fill_fields = None
        self.frame_add_field = None
        self.delete_button = None
        self.edit_button = None
        self.add_button = None
        self.input_class = user_objects.Expense
        self.table_widget = None
        self.main_widget_layout = None
        self.main_widget = None

    def set_up(self, main_widget_name: str = ''):
        self.main_widget = QtWidgets.QWidget()
        self.main_widget.setObjectName(main_widget_name)

        # set layout of main qwidget
        self.main_widget_layout = QVBoxLayout(self.main_widget)

        # create two frames, the one will be the form that someone could enter something
        # and the other will contain the table

        frame_table = create_frame('vertical')
        self.create_table()
        frame_table.layout().addWidget(self.table_widget)

        frame_basic_operation = create_frame('horizontal')
        self.add_button = add_button(frame_basic_operation.layout(), input_icon="plus-circle.svg",
                                     horizontal_policy='Minimum')

        self.add_button.setFixedSize(35, 35)

        self.edit_button = add_button(frame_basic_operation.layout(), input_icon="edit-2.svg",
                                      horizontal_policy='Minimum')
        self.edit_button.setFixedSize(35, 35)
        self.delete_button = add_button(frame_basic_operation.layout(), input_icon="trash-2.svg",
                                        horizontal_policy='Minimum')
        self.delete_button.setFixedSize(35, 35)
        frame_basic_operation.layout().addSpacing(900)

        # include in main_layout
        self.main_widget_layout.addWidget(frame_basic_operation)
        self.main_widget_layout.addWidget(frame_table)

    def create_table(self):

        self.table_widget = QTableWidget()

        # set size policy to expanding
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.table_widget.setSizePolicy(sizePolicy)

        # get all_objects from input class as a list
        all_objects = self.input_class.get()
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

        self.table_widget.setRowCount(0)
        for idx_row, cont in enumerate(all_data_list):
            self.table_widget.insertRow(idx_row)
            flag = False
            if idx_row == 0: flag = True
            for idx_col, item in enumerate(cont.items()):
                print(item)
                if flag:
                    self.table_widget.insertColumn(idx_col)

                self.table_widget.setItem(idx_row, idx_col, QTableWidgetItem(str(item[1])))

        # set column names
        try:
            headers = [i[0] for i in all_data_list[0].items()]
            print(headers)
            for idx, h in enumerate(headers):
                headers[idx] = user_objects.eng_2_greek[h]
            self.table_widget.setHorizontalHeaderLabels(headers)
            style = "::section {""background-color: blue; radius : 12px }"
            self.table_widget.horizontalHeader().setStyleSheet(style)
            self.table_widget.verticalHeader().setStyleSheet(style)
        except IndexError:
            print("do nothing")

    def create_input_form(self):
        """
        This function will create an input form so user can add new expense , income etc
        """
        pass

    def link_buttons(self):
        pass

    def add_item_in_table(self, table, data_dict: {}):
        rowPosition = self.table_widget.rowCount()
        colposition = self.table_widget.columnCount()
        print(rowPosition)
        print(colposition)
        idx_row = self.table_widget.rowCount()
        self.table_widget.insertRow(idx_row)
        for idx_col, item in enumerate(data_dict.items()):
            self.table_widget.setItem(idx_row, idx_col, QTableWidgetItem(str(item[1])))

    def get_widget(self):
        return self.main_widget


class ExpensesPage(BaseEntriesDesign):
    def __init__(self):
        # just define the class and nothing else
        self.minimize_button = None
        self.add_entry_push_button = None
        self.lineEdit_expense_price = None
        self.label_vat = None
        self.frame_non_taxable = None
        self.comboBox_expense_category = None
        self.label_category = None
        self.frame_vat = None
        self.frame_value = None
        self.frame_choose_category = None
        self.frame_1 = None
        self.input_class = user_objects.Expense
        self.set_up()
        self.create_input_form()
        self.main_widget_layout.addWidget(self.frame_add_field, alignment=Qt.AlignmentFlag.AlignCenter)

        # input_form is ready, but we want to be invisible at the start of the program
        main_functionalities.minimize_frame(self.frame_add_field)

        # link buttons
        self.link_buttons()

        # fill comboboxes
        self.fill_expenses_comboboxes()

    def create_input_form(self):
        # first create a frame
        self.frame_add_field = create_frame("vertical")
        self.frame_add_field.setObjectName("frame_add_field")

        # define size policy for this form. Actually we want to be minimized by default
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.frame_add_field.setSizePolicy(sizePolicy)

        # define background color so it could be visible
        self.frame_add_field.setStyleSheet(u"\n"
                                           "background-color: rgb(32, 38, 48)")

        # create fill fields frame
        self.frame_fill_fields = create_frame(layout="horizontal", parent_frame=self.frame_add_field)
        self.frame_fill_fields.setObjectName(u"frame_fill_fields")

        # since there are 5 fields that need to be filled we will split them to tw0 frames for better visibility
        self.frame_1 = create_frame(parent_frame=self.frame_fill_fields)

        # in this frame should be 3 other frames , one for every entry field which contain one label and an entry field
        # choose category frame
        self.frame_choose_category = create_frame(layout="horizontal", parent_frame=self.frame_1)
        self.comboBox_expense_category = QComboBox(self.frame_choose_category)
        self.comboBox_expense_category.setObjectName(u"comboBox_expense_category")
        self.label_category = QLabel(self.frame_choose_category)
        self.label_category.setObjectName(u"label_category")
        self.label_category.setText("Κατηγορία")

        # add widgets and add spacing for better visibility
        self.frame_choose_category.layout().addWidget(self.label_category)
        self.frame_choose_category.layout().addWidget(self.comboBox_expense_category)
        # self.frame_choose_category.layout().addSpacing(600)

        # frame value
        self.frame_value = create_frame(layout="horizontal", parent_frame=self.frame_1)
        self.label_value = QLabel(self.frame_value)
        self.label_value.setObjectName("label_value")
        self.label_value.setText("Ποσό")
        self.lineEdit_expense_price = QLineEdit(self.frame_value)
        self.lineEdit_expense_price.setObjectName("lineEdit_expense_price")

        # add widgets
        self.frame_value.layout().addWidget(self.label_value)
        self.frame_value.layout().addWidget(self.lineEdit_expense_price)
        # self.frame_value.layout().addSpacing(600)

        # frame vat
        self.frame_vat = create_frame(layout="horizontal", parent_frame=self.frame_1)

        self.label_vat = QLabel(self.frame_vat)
        self.label_vat.setObjectName("label_vat")
        self.label_vat.setText("ΦΠΑ")
        self.lineEdit_vat = QLineEdit(self.frame_vat)
        self.lineEdit_expense_price.setObjectName("lineEdit_vat")

        # add widgets
        self.frame_vat.layout().addWidget(self.label_vat)
        self.frame_vat.layout().addWidget(self.lineEdit_vat)

        # and the second frame
        self.frame_2 = create_frame(parent_frame=self.frame_fill_fields)

        # in this frame should be 2 other frames , one for every entry field which contain one label and an entry field
        # choose category frame
        self.frame_choose_type = create_frame(layout="horizontal", parent_frame=self.frame_2)
        self.comboBox_expense_type = QComboBox(self.frame_choose_type)
        self.comboBox_expense_type.setObjectName(u"comboBox_expense_type")
        self.label_type = QLabel(self.frame_choose_type)
        self.label_type.setObjectName(u"label_type")
        self.label_type.setText("Τύπος")

        # add widgets and add spacing for better visibility
        self.frame_choose_type.layout().addWidget(self.label_type)
        self.frame_choose_type.layout().addWidget(self.comboBox_expense_type)
        # self.frame_choose_type.layout().addSpacing(600)

        # frame non_taxable
        self.frame_non_taxable = create_frame(layout="horizontal", parent_frame=self.frame_2)
        self.label_non_taxable = QLabel(self.frame_non_taxable)
        self.label_non_taxable.setObjectName("label_non_taxable")
        self.label_non_taxable.setText("Αποφορολογητέο")
        self.lineEdit_non_taxable = QLineEdit(self.frame_non_taxable)
        self.lineEdit_non_taxable.setObjectName("lineEdit_non_taxable")

        # add widgets
        self.frame_non_taxable.layout().addWidget(self.label_non_taxable)
        self.frame_non_taxable.layout().addWidget(self.lineEdit_non_taxable)
        # self.frame_non_taxable.layout().addSpacing(600)

        self.frame_1.layout().addWidget(self.frame_choose_category)
        self.frame_1.layout().addWidget(self.frame_value)
        self.frame_1.layout().addWidget(self.frame_vat)
        self.frame_fill_fields.layout().addWidget(self.frame_1, alignment=Qt.AlignmentFlag.AlignTop)

        self.frame_2.layout().addWidget(self.frame_choose_type)
        self.frame_2.layout().addWidget(self.frame_non_taxable)
        self.frame_fill_fields.layout().addWidget(self.frame_2, alignment=Qt.AlignmentFlag.AlignTop)

        # create frame_buttons which will have just two buttons one for minimizing and one for adding
        self.frame_buttons = create_frame(layout='horizontal', parent_frame=self.frame_add_field)
        self.minimize_button = add_button(layout=self.frame_buttons.layout(), input_icon="chevron-left.svg")
        self.add_entry_push_button = add_button(layout=self.frame_buttons.layout(), input_icon="plus-circle.svg")

        # add all frames
        self.frame_add_field.layout().addWidget(self.frame_fill_fields)
        self.frame_add_field.layout().addWidget(self.frame_buttons)

        # set maximum size
        self.frame_add_field.setMaximumSize(500, 500)

    def set_get_expense_entry(self):
        """
        create new expense object based on user input
        Returns: dictionary of this object
        """
        new_expense_object = user_objects.Expense(self.comboBox_expense_category.currentText(),
                                                  self.comboBox_expense_type.currentText(),
                                                  int(self.lineEdit_expense_price.text()),
                                                  int(self.lineEdit_non_taxable.text()),
                                                  int(self.lineEdit_vat.text()),
                                                  )
        new_expense_object.save()
        return new_expense_object.to_data_dict()

    def fill_expenses_comboboxes(self):
        main_functionalities.fill_combobox(self.comboBox_expense_category,
                                           user_objects.Expense.FIXED_EXPENSE_CATEGORIES)
        main_functionalities.fill_combobox(self.comboBox_expense_type, user_objects.Expense.TYPES_OF_CHARGE)

    def link_buttons(self):
        # above the table there are 3 buttons add, edit and delete. We may link them with specific actions
        # add button shall make an input form to be appeared
        self.add_button.clicked.connect(lambda: main_functionalities.expand_frame(self.frame_add_field))

        # minimize button shall minimize the add entry frame
        self.minimize_button.clicked.connect(lambda: main_functionalities.minimize_frame(self.frame_add_field))

        # add button shall add new expense
        self.add_entry_push_button.clicked.connect(
            lambda: self.add_item_in_table(self.table_widget, self.set_get_expense_entry()))


class IncomesPage(BaseEntriesDesign):
    def __init__(self):
        # just define the class and nothing else
        self.input_class = user_objects.Income
        self.set_up()


class EmployeesPage(BaseEntriesDesign):
    def __init__(self):
        # just define the class and nothing else
        self.input_class = user_objects.Income
        self.set_up()


class ChartCreator(QChart):

    def __init__(self, datas, parent=None):
        super(ChartCreator, self).__init__(parent)
        self._datas = datas

        self.legend().hide()
        self.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

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


class Pages:
    """
    This class will implement all the main menu pages
    """

    def __init__(self):
        super().__init__()
        self.page_incomes = None
        self.page_expenses = None
        self.page_employees = None
        self.entries_stacked_widget = None
        self.push_button_employees = None
        self.push_button_incomes = None
        self.push_button_expenses = None

    def page_entries(self):
        # set layout
        page_widget = QWidget()
        page_layout = QVBoxLayout(page_widget)
        central_view_frame = create_frame('horizontal')

        # we want this frame to expand so the buttons are only on top!
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        central_view_frame.setSizePolicy(sizePolicy)
        push_buttons_selection_frame = create_frame("horizontal")

        # add corresponding push buttons
        self.push_button_incomes = add_button(push_buttons_selection_frame.layout(), text="Έσοδα")
        self.push_button_expenses = add_button(push_buttons_selection_frame.layout(), text="Έξοδα")
        self.push_button_employees = add_button(push_buttons_selection_frame.layout(), text="Υπάλληλοι")

        page_layout.addWidget(push_buttons_selection_frame, alignment=Qt.AlignmentFlag.AlignTop)

        # at the top we have the selection buttons (incomes,expenses etc) and right above a stacked widget
        central_container_frame = create_frame("horizontal")
        self.entries_stacked_widget = QStackedWidget()

        # create pages
        self.page_incomes = IncomesPage().get_widget()
        self.page_expenses = ExpensesPage().get_widget()
        self.page_employees = EmployeesPage().get_widget()

        # add pages to stacked_widget
        self.entries_stacked_widget.addWidget(self.page_incomes)
        self.entries_stacked_widget.addWidget(self.page_expenses)
        self.entries_stacked_widget.addWidget(self.page_employees)

        # link push buttons to pages
        main_functionalities.link_pages(self.push_button_expenses, self.page_expenses,
                                        self.entries_stacked_widget)
        main_functionalities.link_pages(self.push_button_incomes, self.page_incomes,
                                        self.entries_stacked_widget)
        main_functionalities.link_pages(self.push_button_employees, self.page_employees,
                                        self.entries_stacked_widget)
        # add stacked widget to frame
        central_container_frame.layout().addWidget(self.entries_stacked_widget)
        page_layout.addWidget(central_container_frame)

        return page_widget

    def page_dashboard_set_up(self):
        # define datas
        page_widget = QWidget()
        my_datas = user_objects.Expense.get()
        chart = ChartCreator(my_datas)
        chart.setTitle("Έξοδα")
        title = chart.title()

        chart.setTitleBrush(QBrush(Qt.GlobalColor.white))
        chart.setTitleFont(QFont("Arial", 14))
        chart.setMargins(QMargins(0, 0, 0, 150))
        chart.setBackgroundVisible(False)
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        page_layout = QHBoxLayout(page_widget)
        page_layout.addWidget(chart_view)

        return page_widget


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
        self.page_dashboard = pages_obj.page_dashboard_set_up()

        self.page_entries = pages_obj.page_entries()
        # self.page_entries = ExpensesPage().get_widget()
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
