import unittest

from PyQt6.QtCore import QSize

from src.ui.menu_container import MenuContainer
import sys
import unittest
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QFrame, QVBoxLayout, QPushButton
from PyQt6.QtTest import QTest

app = QApplication(sys.argv)

# create instance of class
menu_container_obj = MenuContainer()


class TestCreateFrame(unittest.TestCase):
    def test_create_frame_with_buttons(self):
        buttons = [1, 2, 3]
        add_space = 10
        frame = menu_container_obj.create_frame(buttons, add_space)

        self.assertIsInstance(frame, QFrame)
        self.assertEqual(frame.frameShape(), QFrame.Shape.StyledPanel)
        self.assertEqual(frame.frameShadow(), QFrame.Shadow.Plain)
        self.assertIsInstance(frame.layout(), QVBoxLayout)

    def test_create_frame_without_buttons(self):
        buttons = []
        add_space = 0
        frame = menu_container_obj.create_frame(buttons, add_space)

        self.assertIsInstance(frame, QFrame)
        self.assertEqual(frame.frameShape(), QFrame.Shape.StyledPanel)
        self.assertEqual(frame.frameShadow(), QFrame.Shadow.Plain)
        self.assertIsInstance(frame.layout(), QVBoxLayout)


class TestAddButton(unittest.TestCase):
    def test_add_button_with_icon(self):
        layout = QVBoxLayout()
        input_icon = 'align-justify.svg'

        menu_container_obj.add_button(layout, input_icon)

        self.assertEqual(layout.count(), 1)
        self.assertIsInstance(layout.itemAt(0).widget(), QPushButton)
        self.assertIsInstance(layout.itemAt(0).widget().icon(), QIcon)

if __name__ == '__main__':
    unittest.main()
