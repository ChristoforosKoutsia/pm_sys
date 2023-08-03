from PyQt6.QtCore import Qt, QRect, QPropertyAnimation, QEasingCurve, pyqtProperty, QSize
from PyQt6.QtWidgets import QMessageBox, QPushButton, QCheckBox
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtGui import QPainter, QColor, QIcon

from global_variables import GlobalVariables


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

class QPushButtonBrightDark(QPushButton):
    """
    A class for implementing the icon's switch on bright and dark mode
    """
    def __init__(self, bright_icon_file, dark_icon_file):
        """

        Args:
            bright_icon_file: The file path containing the icon for bright mode
            dark_icon_file: The file path containing the icon for dark mode

            :type bright_icon_file: str
            :type dark_icon_file: str
        """
        super().__init__()
        self.bright_icon_file = bright_icon_file
        self.dark_icon_file = dark_icon_file

    def set_dark(self):
        """
        Sets icon either to dark or bright mode based on global state of is_dark

        Returns: void
        """
        if GlobalVariables.is_dark:
            self.setIcon(QIcon(self.dark_icon_file))
        else:
            self.setIcon(QIcon(self.bright_icon_file))
        self.setIconSize(QSize(30, 30))

class QToggle(QCheckBox):
    """
    A toggle-like checkbox with a small animation

    """
    def __init__(self, width=40, height=17, bg_color="#777", circle_color="#DDD", active_color="#166e9b"):
        """

        Args:
            width: Button's width
            height: Button's height
            bg_color: Background color
            circle_color: Circle's color
            active_color: Color of background when button is active

        """
        super().__init__()

        # Set default parameters
        self.setFixedSize(width, height)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        # Set colors
        self._width = width
        self._height = height
        self._bg_color = bg_color
        self._circle_color = circle_color
        self._active_color = active_color

        # Create animation
        self._circle_position = 2
        self.animation = QPropertyAnimation(self, b"circle_position", self)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animation.setDuration(300)

        self.stateChanged.connect(self.start_animation)

    def start_animation(self, state):
        """
        A function to implement the animation

        Args:
            state: It defines whether the checkbox is checked or not

        Returns: void

        """
        self.animation.stop()
        if state:
            self.animation.setEndValue(self.height() + 2*4)
        else:
            self.animation.setEndValue(2)
        self.animation.start()

    @pyqtProperty(int)
    def circle_position(self):
        return self._circle_position

    @circle_position.setter
    def circle_position(self, pos):
        self._circle_position = pos
        self.update()


    def hitButton(self, pos: QtCore.QPoint) -> bool:
        return self.contentsRect().contains(pos)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        # Set painter
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Set as no pen
        p.setPen(Qt.PenStyle.NoPen)

        # Draw rectangle
        rect = QRect(0, 0, self.width(), self.height())

        if not self.isChecked():
            # Draw background
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)

            # Draw circle
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position, 2, self._height - 4, self._height - 4)
        else:
            # Draw background
            p.setBrush(QColor(self._active_color))
            p.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)

            # Draw circle
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position, 2, self._height - 4, self._height - 4)

        # End raw
        p.end()