from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal


class CalcControlWidget(QWidget):
    switched = pyqtSignal(str)

    def calc_mode_switch(self):
        radiobtn = self.sender()
        if radiobtn.isChecked():
            text = radiobtn.text()
            self.switched.emit(text)

    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        radiobutton = QRadioButton(text='Default')
        radiobutton.setChecked(True)
        radiobutton.toggled.connect(self.calc_mode_switch)
        main_layout.addWidget(radiobutton)
        radiobutton.setStyleSheet('color: rgb(255, 255, 255)')
        radiobutton.setFont(QFont("Times", 10))

        radiobutton2 = QRadioButton(text='ACC')
        radiobutton2.toggled.connect(self.calc_mode_switch)
        main_layout.addWidget(radiobutton2)
        radiobutton2.setStyleSheet('color: rgb(255, 255, 255)')
        radiobutton2.setFont(QFont("Times", 10))

        radiobutton3 = QRadioButton(text='MATH')
        radiobutton3.toggled.connect(self.calc_mode_switch)
        main_layout.addWidget(radiobutton3)
        radiobutton3.setStyleSheet('color: rgb(255, 255, 255)')
        radiobutton3.setFont(QFont("Times", 10))