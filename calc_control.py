from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
class CalcControlWidget(QWidget):
    switched : pyqtSignal = None
    def calc_mode_switch(self):
        radiobtn = self.sender()
        if radiobtn.isChecked():
            text = radiobtn.text()
            self.switched.emit(text)

    def __init__(self):
        super().__init__()
        self.switched = pyqtSignal(str)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        radioBtn = QRadioButton(text="Простой")
        radioBtn.setChecked(True)
        radioBtn.toggled.connect(self.calc_mode_switch)
        main_layout.addWidget(radioBtn)

        radioBtn1 = QRadioButton(text= 'Бухгалтерский')
        radioBtn1.toggled.connect(self.calc_mode_switch)
        main_layout.addWidget(radioBtn1)
