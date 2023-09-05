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

        radiobutton = QRadioButton(text='Simple')
        radiobutton.setChecked(True)
        radiobutton.toggled.connect(self.calc_mode_switch)
        main_layout.addWidget(radiobutton)

        radiobutton2 = QRadioButton(text='Account')
        radiobutton2.toggled.connect(self.calc_mode_switch)
        main_layout.addWidget(radiobutton2)