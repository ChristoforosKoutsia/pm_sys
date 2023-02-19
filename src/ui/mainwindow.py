# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1205, 794)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"*{\n"
"padding :0;\n"
"border : none;\n"
"margin : 0;\n"
"background : none;\n"
"background-color : transparent;\n"
"color : #fff\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color: #1f232a;\n"
"radius : 12px\n"
"}\n"
"#leftMenuSubContainer{\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"#leftMenuSubContainer QPushButton{\n"
"text-align:left;\n"
"padding:15px;\n"
"border-top-left-radius :10px;\n"
"border-bottom-left-radius : 10px;\n"
"background-color: #1f232a;\n"
"\n"
"}\n"
"\n"
"#leftMenuSubContainer QPushButton:hover\n"
"{\n"
"   background-color:rgb(184, 227, 255);\n"
"cursor :pointer ;\n"
"}\n"
"\n"
"#mainBodyContainer QPushButton{\n"
"text-align:center;\n"
"padding:10px ,10px ;\n"
"border-top-left-radius :10px;\n"
"border-bottom-left-radius : 10px;\n"
"border-top-right-radius :10px;\n"
"border-bottom-right-radius : 10px;\n"
"background-color: #16191d;\n"
"border-right-color: rgb(255, 46, 60);\n"
"}\n"
" \n"
"#frame_8 QPushButton{\n"
"text-align:center;\n"
"padding:5px ;\n"
"border-top-left-radius :0px;"
                        "\n"
"border-bottom-left-radius : 0px;\n"
"border-top-right-radius :0px;\n"
"border-bottom-right-radius : 0px;\n"
"background-color: #rgb(171, 171, 171);\n"
"}\n"
"\n"
"\n"
"QLineEdit {\n"
" border: 1px solid white;\n"
"}\n"
"\n"
"QComboBox {\n"
" border: 1px solid white;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftMenuContainer = QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 10)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/feather/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 30))
        self.pushButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pushButton, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.dashboard_pushButton = QPushButton(self.frame_2)
        self.dashboard_pushButton.setObjectName(u"dashboard_pushButton")
        self.dashboard_pushButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/feather/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_pushButton.setIcon(icon1)
        self.dashboard_pushButton.setIconSize(QSize(20, 20))
        self.dashboard_pushButton.setFlat(False)

        self.verticalLayout_3.addWidget(self.dashboard_pushButton)

        self.entries_pushButton = QPushButton(self.frame_2)
        self.entries_pushButton.setObjectName(u"entries_pushButton")
        self.entries_pushButton.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/feather/archive.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.entries_pushButton.setIcon(icon2)
        self.entries_pushButton.setIconSize(QSize(20, 20))
        self.entries_pushButton.setFlat(False)

        self.verticalLayout_3.addWidget(self.entries_pushButton)

        self.account_pushButton = QPushButton(self.frame_2)
        self.account_pushButton.setObjectName(u"account_pushButton")
        self.account_pushButton.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/feather/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.account_pushButton.setIcon(icon3)
        self.account_pushButton.setIconSize(QSize(20, 20))
        self.account_pushButton.setFlat(False)

        self.verticalLayout_3.addWidget(self.account_pushButton)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.help_pushButton = QPushButton(self.frame_3)
        self.help_pushButton.setObjectName(u"help_pushButton")
        self.help_pushButton.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/feather/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.help_pushButton.setIcon(icon4)
        self.help_pushButton.setIconSize(QSize(20, 20))
        self.help_pushButton.setFlat(False)

        self.verticalLayout_4.addWidget(self.help_pushButton)

        self.settings_pushButton = QPushButton(self.frame_3)
        self.settings_pushButton.setObjectName(u"settings_pushButton")
        self.settings_pushButton.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/feather/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_pushButton.setIcon(icon5)
        self.settings_pushButton.setIconSize(QSize(20, 20))
        self.settings_pushButton.setFlat(False)

        self.verticalLayout_4.addWidget(self.settings_pushButton)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy2)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.main_menu_selection = QStackedWidget(self.mainBodyContainer)
        self.main_menu_selection.setObjectName(u"main_menu_selection")
        self.page_dashboard = QWidget()
        self.page_dashboard.setObjectName(u"page_dashboard")
        self.main_menu_selection.addWidget(self.page_dashboard)
        self.page_entries = QWidget()
        self.page_entries.setObjectName(u"page_entries")
        self.verticalLayout_6 = QVBoxLayout(self.page_entries)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.mainBody = QWidget(self.page_entries)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy2.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy2)
        self.mainBody.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.mainBody)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.push_buttons_selection = QFrame(self.mainBody)
        self.push_buttons_selection.setObjectName(u"push_buttons_selection")
        self.push_buttons_selection.setFrameShape(QFrame.StyledPanel)
        self.push_buttons_selection.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.push_buttons_selection)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.incomes_pushButton = QPushButton(self.push_buttons_selection)
        self.incomes_pushButton.setObjectName(u"incomes_pushButton")

        self.horizontalLayout_7.addWidget(self.incomes_pushButton)

        self.expenses_pushButton = QPushButton(self.push_buttons_selection)
        self.expenses_pushButton.setObjectName(u"expenses_pushButton")

        self.horizontalLayout_7.addWidget(self.expenses_pushButton)

        self.employees_pushButton = QPushButton(self.push_buttons_selection)
        self.employees_pushButton.setObjectName(u"employees_pushButton")

        self.horizontalLayout_7.addWidget(self.employees_pushButton)


        self.verticalLayout_7.addWidget(self.push_buttons_selection)

        self.central_container = QFrame(self.mainBody)
        self.central_container.setObjectName(u"central_container")
        sizePolicy.setHeightForWidth(self.central_container.sizePolicy().hasHeightForWidth())
        self.central_container.setSizePolicy(sizePolicy)
        self.central_container.setFrameShape(QFrame.StyledPanel)
        self.central_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.central_container)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.entries_stackwidget = QStackedWidget(self.central_container)
        self.entries_stackwidget.setObjectName(u"entries_stackwidget")
        self.page_incomes = QWidget()
        self.page_incomes.setObjectName(u"page_incomes")
        self.horizontalLayout_3 = QHBoxLayout(self.page_incomes)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_add_incomes = QFrame(self.page_incomes)
        self.frame_add_incomes.setObjectName(u"frame_add_incomes")
        self.frame_add_incomes.setFrameShape(QFrame.StyledPanel)
        self.frame_add_incomes.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_add_incomes)

        self.frame_overview_incomes = QFrame(self.page_incomes)
        self.frame_overview_incomes.setObjectName(u"frame_overview_incomes")
        sizePolicy2.setHeightForWidth(self.frame_overview_incomes.sizePolicy().hasHeightForWidth())
        self.frame_overview_incomes.setSizePolicy(sizePolicy2)
        self.frame_overview_incomes.setFrameShape(QFrame.StyledPanel)
        self.frame_overview_incomes.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_overview_incomes)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_46 = QFrame(self.frame_overview_incomes)
        self.frame_46.setObjectName(u"frame_46")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_46.sizePolicy().hasHeightForWidth())
        self.frame_46.setSizePolicy(sizePolicy3)
        self.frame_46.setMaximumSize(QSize(889, 653))
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.new_income_pushButton_9 = QPushButton(self.frame_46)
        self.new_income_pushButton_9.setObjectName(u"new_income_pushButton_9")
        icon6 = QIcon()
        icon6.addFile(u":/icons/feather/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.new_income_pushButton_9.setIcon(icon6)

        self.horizontalLayout_16.addWidget(self.new_income_pushButton_9)

        self.edit_income_pushButton_9 = QPushButton(self.frame_46)
        self.edit_income_pushButton_9.setObjectName(u"edit_income_pushButton_9")
        icon7 = QIcon()
        icon7.addFile(u":/icons/feather/edit-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_income_pushButton_9.setIcon(icon7)

        self.horizontalLayout_16.addWidget(self.edit_income_pushButton_9)

        self.delete_income_pushButton_9 = QPushButton(self.frame_46)
        self.delete_income_pushButton_9.setObjectName(u"delete_income_pushButton_9")
        icon8 = QIcon()
        icon8.addFile(u":/icons/feather/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_income_pushButton_9.setIcon(icon8)

        self.horizontalLayout_16.addWidget(self.delete_income_pushButton_9)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_9)

        self.pushButton_explore_9 = QPushButton(self.frame_46)
        self.pushButton_explore_9.setObjectName(u"pushButton_explore_9")

        self.horizontalLayout_16.addWidget(self.pushButton_explore_9)


        self.verticalLayout_12.addWidget(self.frame_46)

        self.incomes_tableWidget_9 = QTableWidget(self.frame_overview_incomes)
        self.incomes_tableWidget_9.setObjectName(u"incomes_tableWidget_9")
        sizePolicy.setHeightForWidth(self.incomes_tableWidget_9.sizePolicy().hasHeightForWidth())
        self.incomes_tableWidget_9.setSizePolicy(sizePolicy)

        self.verticalLayout_12.addWidget(self.incomes_tableWidget_9)


        self.horizontalLayout_3.addWidget(self.frame_overview_incomes)

        self.entries_stackwidget.addWidget(self.page_incomes)
        self.page_expenses = QWidget()
        self.page_expenses.setObjectName(u"page_expenses")
        self.horizontalLayout_9 = QHBoxLayout(self.page_expenses)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_add_expense = QFrame(self.page_expenses)
        self.frame_add_expense.setObjectName(u"frame_add_expense")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(100)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_add_expense.sizePolicy().hasHeightForWidth())
        self.frame_add_expense.setSizePolicy(sizePolicy4)
        self.frame_add_expense.setStyleSheet(u"\n"
"background-color: rgb(48, 40, 70)")
        self.frame_add_expense.setFrameShape(QFrame.StyledPanel)
        self.frame_add_expense.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_add_expense)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_fill_fields = QFrame(self.frame_add_expense)
        self.frame_fill_fields.setObjectName(u"frame_fill_fields")
        sizePolicy3.setHeightForWidth(self.frame_fill_fields.sizePolicy().hasHeightForWidth())
        self.frame_fill_fields.setSizePolicy(sizePolicy3)
        self.frame_fill_fields.setFrameShape(QFrame.StyledPanel)
        self.frame_fill_fields.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_fill_fields)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_6 = QFrame(self.frame_fill_fields)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy3.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy3)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_35 = QFrame(self.frame_6)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_3 = QLabel(self.frame_35)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_19.addWidget(self.label_3)

        self.comboBox_expense_category = QComboBox(self.frame_35)
        self.comboBox_expense_category.setObjectName(u"comboBox_expense_category")

        self.horizontalLayout_19.addWidget(self.comboBox_expense_category)


        self.verticalLayout_16.addWidget(self.frame_35)

        self.frame_44 = QFrame(self.frame_6)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_4 = QLabel(self.frame_44)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout_18.addWidget(self.label_4, 0, Qt.AlignRight)

        self.lineEdit_expense_price = QLineEdit(self.frame_44)
        self.lineEdit_expense_price.setObjectName(u"lineEdit_expense_price")

        self.horizontalLayout_18.addWidget(self.lineEdit_expense_price)


        self.verticalLayout_16.addWidget(self.frame_44)

        self.frame_47 = QFrame(self.frame_6)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_5 = QLabel(self.frame_47)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_17.addWidget(self.label_5)

        self.lineEdit_expense_vat = QLineEdit(self.frame_47)
        self.lineEdit_expense_vat.setObjectName(u"lineEdit_expense_vat")

        self.horizontalLayout_17.addWidget(self.lineEdit_expense_vat)


        self.verticalLayout_16.addWidget(self.frame_47)


        self.horizontalLayout_4.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.frame_7 = QFrame(self.frame_fill_fields)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy3.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy3)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_7)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.comboBox_expense_type = QComboBox(self.frame_8)
        self.comboBox_expense_type.setObjectName(u"comboBox_expense_type")

        self.horizontalLayout_5.addWidget(self.comboBox_expense_type)


        self.verticalLayout_15.addWidget(self.frame_8)

        self.frame_34 = QFrame(self.frame_7)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.frame_34)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.lineEdit_expense_non_taxable_price = QLineEdit(self.frame_34)
        self.lineEdit_expense_non_taxable_price.setObjectName(u"lineEdit_expense_non_taxable_price")

        self.horizontalLayout_6.addWidget(self.lineEdit_expense_non_taxable_price)


        self.verticalLayout_15.addWidget(self.frame_34)


        self.horizontalLayout_4.addWidget(self.frame_7, 0, Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.frame_fill_fields)

        self.frame_buttons = QFrame(self.frame_add_expense)
        self.frame_buttons.setObjectName(u"frame_buttons")
        sizePolicy3.setHeightForWidth(self.frame_buttons.sizePolicy().hasHeightForWidth())
        self.frame_buttons.setSizePolicy(sizePolicy3)
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_buttons)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pushButton_save_expense = QPushButton(self.frame_buttons)
        self.pushButton_save_expense.setObjectName(u"pushButton_save_expense")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_save_expense.sizePolicy().hasHeightForWidth())
        self.pushButton_save_expense.setSizePolicy(sizePolicy5)
        self.pushButton_save_expense.setMaximumSize(QSize(167, 16777215))
        self.pushButton_save_expense.setIcon(icon6)

        self.horizontalLayout_20.addWidget(self.pushButton_save_expense)

        self.pushButton_minimize_form = QPushButton(self.frame_buttons)
        self.pushButton_minimize_form.setObjectName(u"pushButton_minimize_form")
        icon9 = QIcon()
        icon9.addFile(u":/icons/feather/chevron-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_minimize_form.setIcon(icon9)

        self.horizontalLayout_20.addWidget(self.pushButton_minimize_form, 0, Qt.AlignRight)


        self.verticalLayout_13.addWidget(self.frame_buttons)


        self.horizontalLayout_9.addWidget(self.frame_add_expense, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_table_expenses = QFrame(self.page_expenses)
        self.frame_table_expenses.setObjectName(u"frame_table_expenses")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(100)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_table_expenses.sizePolicy().hasHeightForWidth())
        self.frame_table_expenses.setSizePolicy(sizePolicy6)
        self.frame_table_expenses.setFrameShape(QFrame.StyledPanel)
        self.frame_table_expenses.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_table_expenses)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_38 = QFrame(self.frame_table_expenses)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy2.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy2)
        self.frame_38.setMaximumSize(QSize(889, 653))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.new_expense_pushButton = QPushButton(self.frame_38)
        self.new_expense_pushButton.setObjectName(u"new_expense_pushButton")
        self.new_expense_pushButton.setIcon(icon6)

        self.horizontalLayout_10.addWidget(self.new_expense_pushButton)

        self.edit_expense_pushButton = QPushButton(self.frame_38)
        self.edit_expense_pushButton.setObjectName(u"edit_expense_pushButton")
        self.edit_expense_pushButton.setIcon(icon7)

        self.horizontalLayout_10.addWidget(self.edit_expense_pushButton)

        self.delete_expense_pushButton = QPushButton(self.frame_38)
        self.delete_expense_pushButton.setObjectName(u"delete_expense_pushButton")
        self.delete_expense_pushButton.setIcon(icon8)

        self.horizontalLayout_10.addWidget(self.delete_expense_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.pushButton_explore = QPushButton(self.frame_38)
        self.pushButton_explore.setObjectName(u"pushButton_explore")

        self.horizontalLayout_10.addWidget(self.pushButton_explore)


        self.verticalLayout_8.addWidget(self.frame_38)

        self.expenses_tableWidget = QTableWidget(self.frame_table_expenses)
        self.expenses_tableWidget.setObjectName(u"expenses_tableWidget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.expenses_tableWidget.sizePolicy().hasHeightForWidth())
        self.expenses_tableWidget.setSizePolicy(sizePolicy7)

        self.verticalLayout_8.addWidget(self.expenses_tableWidget)


        self.horizontalLayout_9.addWidget(self.frame_table_expenses)

        self.entries_stackwidget.addWidget(self.page_expenses)

        self.horizontalLayout_8.addWidget(self.entries_stackwidget)


        self.verticalLayout_7.addWidget(self.central_container)


        self.verticalLayout_6.addWidget(self.mainBody)

        self.main_menu_selection.addWidget(self.page_entries)
        self.page_account = QWidget()
        self.page_account.setObjectName(u"page_account")
        self.main_menu_selection.addWidget(self.page_account)

        self.verticalLayout_5.addWidget(self.main_menu_selection)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton.setDefault(False)
        self.dashboard_pushButton.setDefault(False)
        self.entries_pushButton.setDefault(False)
        self.account_pushButton.setDefault(False)
        self.help_pushButton.setDefault(False)
        self.settings_pushButton.setDefault(False)
        self.main_menu_selection.setCurrentIndex(0)
        self.entries_stackwidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"information", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText("")
#if QT_CONFIG(tooltip)
        self.dashboard_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"information", None))
#endif // QT_CONFIG(tooltip)
        self.dashboard_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u03a0\u03af\u03bd\u03b1\u03ba\u03b1\u03c2 \u0395\u03bb\u03ad\u03b3\u03c7\u03bf\u03c5", None))
#if QT_CONFIG(tooltip)
        self.entries_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"information", None))
#endif // QT_CONFIG(tooltip)
        self.entries_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u039a\u03b1\u03c4\u03b1\u03c7\u03c9\u03c1\u03ae\u03c3\u03b5\u03b9\u03c2", None))
#if QT_CONFIG(tooltip)
        self.account_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"information", None))
#endif // QT_CONFIG(tooltip)
        self.account_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u039b\u03bf\u03b3\u03b1\u03c1\u03b9\u03c3\u03b1\u03bc\u03cc\u03c2", None))
#if QT_CONFIG(tooltip)
        self.help_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"information", None))
#endif // QT_CONFIG(tooltip)
        self.help_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0392\u03bf\u03ae\u03b8\u03b5\u03b9\u03b1", None))
#if QT_CONFIG(tooltip)
        self.settings_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"information", None))
#endif // QT_CONFIG(tooltip)
        self.settings_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u03a1\u03c5\u03b8\u03bc\u03af\u03c3\u03b5\u03b9\u03c2", None))
        self.incomes_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0388\u03c3\u03bf\u03b4\u03b1", None))
        self.expenses_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0388\u03be\u03bf\u03b4\u03b1", None))
        self.employees_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u03a5\u03c0\u03ac\u03bb\u03bb\u03b7\u03bb\u03bf\u03b9", None))
        self.new_income_pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u03a0\u03c1\u03bf\u03c3\u03b8\u03ae\u03ba\u03b7", None))
        self.edit_income_pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u0395\u03c0\u03b5\u03be\u03b5\u03c1\u03b3\u03b1\u03c3\u03af\u03b1", None))
        self.delete_income_pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u0394\u03b9\u03b1\u03b3\u03c1\u03b1\u03c6\u03ae", None))
        self.pushButton_explore_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u03a0\u03bf\u03c3\u03cc(\u20ac)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u03a6\u03a0\u0391(%)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u03a4\u03cd\u03c0\u03bf\u03c2", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0391\u03c0\u03bf\u03c6\u03bf\u03c1\u03bf\u03bb\u03bf\u03b3\u03b7\u03c4\u03ad\u03bf(\u20ac)", None))
        self.pushButton_save_expense.setText(QCoreApplication.translate("MainWindow", u"\u03a0\u03c1\u03bf\u03c3\u03b8\u03ae\u03ba\u03b7", None))
        self.pushButton_minimize_form.setText("")
        self.new_expense_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u03a0\u03c1\u03bf\u03c3\u03b8\u03ae\u03ba\u03b7", None))
        self.edit_expense_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0395\u03c0\u03b5\u03be\u03b5\u03c1\u03b3\u03b1\u03c3\u03af\u03b1", None))
        self.delete_expense_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0394\u03b9\u03b1\u03b3\u03c1\u03b1\u03c6\u03ae", None))
        self.pushButton_explore.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

