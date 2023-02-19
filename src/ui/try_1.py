# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'try_1.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QToolBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1258, 642)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setTabletTracking(False)
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setStyleSheet(u"background-color: rgb(57, 59, 59);\n"
"border-top-color: rgb(57, 95, 76);\n"
"border-radius: 40px")
        self.side_menu_bar = QWidget(self.centralwidget)
        self.side_menu_bar.setObjectName(u"side_menu_bar")
        self.side_menu_bar.setGeometry(QRect(0, 30, 221, 571))
        self.side_menu_bar.setStyleSheet(u"background-color: rgb(139, 139, 139);\n"
"background-color: rgb(103, 103, 103);\n"
"border-radius: 11px; \n"
"")
        self.pushButton_entries = QPushButton(self.side_menu_bar)
        self.pushButton_entries.setObjectName(u"pushButton_entries")
        self.pushButton_entries.setGeometry(QRect(20, 130, 171, 31))
        self.pushButton_entries.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_entries.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(138, 138, 138);\n"
"font: 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(184, 227, 255)\n"
"}")
        self.pushButton_3 = QPushButton(self.side_menu_bar)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 210, 171, 31))
        self.pushButton_3.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(138, 138, 138);\n"
"font: 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(184, 227, 255)\n"
"}")
        self.pushButton_dashboard = QPushButton(self.side_menu_bar)
        self.pushButton_dashboard.setObjectName(u"pushButton_dashboard")
        self.pushButton_dashboard.setGeometry(QRect(20, 50, 171, 31))
        self.pushButton_dashboard.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_dashboard.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(138, 138, 138);\n"
"font: 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(184, 227, 255)\n"
"}")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(230, 30, 1101, 631))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(130, 130, 130);\n"
"background-color: rgb(76, 76, 76);\n"
"border-radius: 11px; ")
        self.entries = QWidget()
        self.entries.setObjectName(u"entries")
        self.pushButton_employees = QPushButton(self.entries)
        self.pushButton_employees.setObjectName(u"pushButton_employees")
        self.pushButton_employees.setGeometry(QRect(150, 10, 221, 22))
        self.pushButton_employees.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_employees.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(138, 138, 138);\n"
"font: 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(184, 227, 255)\n"
"}")
        self.push_button_expenses = QPushButton(self.entries)
        self.push_button_expenses.setObjectName(u"push_button_expenses")
        self.push_button_expenses.setGeometry(QRect(530, 10, 201, 22))
        self.push_button_expenses.setCursor(QCursor(Qt.OpenHandCursor))
        self.push_button_expenses.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(138, 138, 138);\n"
"font: 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(184, 227, 255)\n"
"}")
        self.pushButton_incomes = QPushButton(self.entries)
        self.pushButton_incomes.setObjectName(u"pushButton_incomes")
        self.pushButton_incomes.setGeometry(QRect(840, 10, 211, 22))
        self.pushButton_incomes.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_incomes.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(138, 138, 138);\n"
"font: 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(184, 227, 255)\n"
"}")
        self.stackedWidget_2 = QStackedWidget(self.entries)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(40, 50, 791, 531))
        self.stackedWidget_2.setLayoutDirection(Qt.LeftToRight)
        self.stackedWidget_2.setStyleSheet(u"background-color: rgb(77, 77, 77);\n"
"border-color: rgb(255, 101, 181);\n"
"")
        self.page_expenses_3 = QWidget()
        self.page_expenses_3.setObjectName(u"page_expenses_3")
        self.add_newExpense_Widget = QWidget(self.page_expenses_3)
        self.add_newExpense_Widget.setObjectName(u"add_newExpense_Widget")
        self.add_newExpense_Widget.setGeometry(QRect(-10, 30, 411, 301))
        self.fixed_expenses_box = QComboBox(self.add_newExpense_Widget)
        self.fixed_expenses_box.setObjectName(u"fixed_expenses_box")
        self.fixed_expenses_box.setGeometry(QRect(20, 60, 161, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fixed_expenses_box.sizePolicy().hasHeightForWidth())
        self.fixed_expenses_box.setSizePolicy(sizePolicy)
        self.fixed_expenses_box.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"border-radius  : 10 px;\n"
"radius  : 10 px")
        self.type_of_chargecomboBox = QComboBox(self.add_newExpense_Widget)
        self.type_of_chargecomboBox.setObjectName(u"type_of_chargecomboBox")
        self.type_of_chargecomboBox.setGeometry(QRect(260, 60, 151, 31))
        self.type_of_chargecomboBox.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"border-radius  : 10 px;\n"
"radius  : 10 px")
        self.textEdit_4 = QTextEdit(self.add_newExpense_Widget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(30, 150, 71, 31))
        self.textEdit_4.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"border-radius  : 10 px;\n"
"radius  : 10 px")
        self.textEdit_6 = QTextEdit(self.add_newExpense_Widget)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(130, 150, 161, 31))
        self.textEdit_6.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"border-radius  : 10 px;\n"
"radius  : 10 px")
        self.textEdit_8 = QTextEdit(self.add_newExpense_Widget)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setGeometry(QRect(320, 150, 71, 31))
        self.textEdit_8.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"border-radius  : 10 px;\n"
"radius  : 10 px")
        self.tableWidget_expenses = QTableWidget(self.page_expenses_3)
        self.tableWidget_expenses.setObjectName(u"tableWidget_expenses")
        self.tableWidget_expenses.setGeometry(QRect(440, -10, 431, 421))
        self.tableWidget_expenses.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.173, y1:0.556818, x2:1, y2:0, stop:0 rgba(85, 173, 154, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"border-radius: 15px; \n"
"\n"
"selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5,\n"
"                                stop: 0 #FF92BB, stop: 1 white);")
        self.pushButton_newExpense = QPushButton(self.page_expenses_3)
        self.pushButton_newExpense.setObjectName(u"pushButton_newExpense")
        self.pushButton_newExpense.setGeometry(QRect(180, 400, 191, 31))
        self.pushButton_newExpense.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_newExpense.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(78, 149, 90);\n"
"font: 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(184, 227, 255)\n"
"}")
        self.stackedWidget_2.addWidget(self.page_expenses_3)
        self.page_incomes = QWidget()
        self.page_incomes.setObjectName(u"page_incomes")
        self.tableWidget_incomes = QTableWidget(self.page_incomes)
        if (self.tableWidget_incomes.columnCount() < 5):
            self.tableWidget_incomes.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_incomes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_incomes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_incomes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_incomes.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_incomes.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_incomes.setObjectName(u"tableWidget_incomes")
        self.tableWidget_incomes.setGeometry(QRect(170, 100, 481, 281))
        self.tableWidget_incomes.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.173, y1:0.556818, x2:1, y2:0, stop:0 rgba(85, 173, 154, 255), stop:1 rgba(255, 255, 255, 255));")
        self.stackedWidget_2.addWidget(self.page_incomes)
        self.stackedWidget.addWidget(self.entries)
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.textEdit = QTextEdit(self.dashboard)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(130, 140, 441, 291))
        self.stackedWidget.addWidget(self.dashboard)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1258, 21))
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_entries.setText(QCoreApplication.translate("MainWindow", u"\u039a\u03b1\u03c4\u03b1\u03c7\u03c9\u03c1\u03ae\u03c3\u03b5\u03b9\u03c2", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u039b\u03bf\u03b3\u03b1\u03c1\u03b9\u03b1\u03c3\u03bc\u03cc\u03c2", None))
        self.pushButton_dashboard.setText(QCoreApplication.translate("MainWindow", u"\u03a0\u03af\u03bd\u03b1\u03ba\u03b1\u03c2 \u0395\u03bb\u03ad\u03b3\u03c7\u03bf\u03c5", None))
        self.pushButton_employees.setText(QCoreApplication.translate("MainWindow", u"\u0388\u03c3\u03bf\u03b4\u03b1", None))
        self.push_button_expenses.setText(QCoreApplication.translate("MainWindow", u"\u0388\u03be\u03bf\u03b4\u03b1", None))
        self.pushButton_incomes.setText(QCoreApplication.translate("MainWindow", u"\u03a5\u03c0\u03ac\u03bb\u03bb\u03b7\u03bb\u03bf\u03b9", None))
        self.pushButton_newExpense.setText(QCoreApplication.translate("MainWindow", u"\u039d\u03b5\u03cc \u0388\u03be\u03bf\u03b4\u03bf", None))
        ___qtablewidgetitem = self.tableWidget_incomes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem1 = self.tableWidget_incomes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem2 = self.tableWidget_incomes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem3 = self.tableWidget_incomes.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem4 = self.tableWidget_incomes.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">Surprise Motherfucker</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:28pt;\"><br /></p></body></html>", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

