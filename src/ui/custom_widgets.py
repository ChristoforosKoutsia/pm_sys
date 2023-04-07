from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox, QPushButton
from PyQt6 import QtWidgets, QtCore


class CustomMessageBox(QMessageBox):
    def __init__(self, text, info_text, icon=QMessageBox.information):
        super().__init__()
        self.setWindowTitle("Message")
        self.setText(text)
        self.setInformativeText(info_text)
        self.setIcon(icon)
        ok_button = self.addButton("OK", QMessageBox.ButtonRole.AcceptRole)
        ok_button.setStyleSheet("padding: 5px; width: 60px;")
        self.setStyleSheet("""
  QMessageBox {
                background-color: #323232;
                color: white;
                border: none;
                border-radius: 10px;
            }
            QMessageBox QPushButton {
                background-color: #0a84ff;
                color: white;
                padding: 5px;
                border: none;
                border-radius: 5px;
            }
            QMessageBox QPushButton:hover {
                background-color: #0c66d9;
            }
        """)
        self.setDefaultButton(ok_button)

    def run(self):
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.exec()


