import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class My_calculator(QWidget):

    def on_button_pressed(self):
        btn = self.sender()
        key_text = btn.text()
        print(key_text)
        self.calc_model.command(key_text)
        self.main_display.setText(self.calc_model.get_display())

    def keyPressEvent(self, event):
        key_text = event.text()
        self.calc_model.command(key_text)
        self.main_display.setText(self.calc_model.get_display())
        super().keyPressEvent(event)

    def __init__(self, title=None):
        super().__init__()
        self.setStyleSheet("background-color: black;")
        self.setWindowTitle(title)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.result_label = QLabel('0')
        self.result_label.setAlignment(Qt.AlignRight)
        self.result_label.setStyleSheet('color: rgb(255, 255, 255)')
        self.result_label.setFont(QFont("Times", 32))
        layout.addWidget(self.result_label)

        button_grid = QGridLayout()
        layout.addLayout(button_grid)

        buttons = (('AC', 'C', '?', '/'),
                   ('7',  '8', '9', '*'),
                   ('4',  '5', '6', '-'),
                   ('1',  '2', '3', '+'),
                   ('0',  '',  '.', '='))


        for r in range(len(buttons)):
            for c in range(len(buttons[r])):
                key = buttons[r][c]
                if key:
                    btn = QPushButton(text=key)
                    btn.clicked.connect(self.on_button_pressed)
                    if key != '0':
                        button_grid.addWidget(btn, r, c)
                    else:
                        button_grid.addWidget(btn, r, c, 1, 2)
                btn.setStyleSheet("background-color : orange")

