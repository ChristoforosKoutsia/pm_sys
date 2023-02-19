"""
This module will contain class that implements base functionalities
"""
from abc import ABC

from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QHBoxLayout, QStackedWidget


def link_pages(button: QPushButton, page: QtWidgets.QWidget, stacked_widget: QStackedWidget):
    button.clicked.connect(lambda: stacked_widget.setCurrentWidget(page))


class BaseFunctionalities(ABC):
    """
    Abstract class which implements base functions with PyQt like create frames and add_buttons
    """

    def __init__(self):
        super().__init__()

    def create_frame(self, layout='vertical'):
        '''
        This is a function to set frames on the left side menu
        Inputs :
            - add_space : int that indicates if current layout (frame) will have some space w.r.t to others
                          Actually,adds a non-stretchable area (aQSpacerItem) of int value to the layout
        Returns :
            The created frame with all buttons
        '''
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.StyledPanel)
        frame.setFrameShadow(QFrame.Shadow.Plain)
        # set layout of frame_2

        if layout == 'vertical':
            layout_frame = QVBoxLayout(frame)
        else:
            layout_frame = QHBoxLayout(frame)
        return frame

    def add_button(self, layout, input_icon='', alignment='', text=""):
        '''
        Args:
            text: text that will be displayed in the button
            alignment: alignment of the button in the given layout,
            layout: the layout that push_button will be imported
            input_icon: if push button have icon then the name of svg should be passed(e.g align-justify.svg)

        Returns:
            Created push button in given layout
        '''
        push_button = QPushButton()
        if input_icon:
            icon = QIcon()
            # icon.addFile(f":/icons/feather/{input_icon}")
            icon.addFile(f"../../ui/img/feather/{input_icon}")
            push_button.setIcon(icon)
            push_button.setIconSize(QSize(30, 30))
        push_button.setText(text)
        layout.addWidget(push_button, alignment=Qt.AlignmentFlag.AlignLeft)

        return push_button
