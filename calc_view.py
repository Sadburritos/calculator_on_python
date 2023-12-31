from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class SimpleCalcView(QWidget):
    main_display: QLabel = None
    calc_model = None

    def on_button_pressed(self):
        btn = self.sender()
        key_text = btn.text()
        print(key_text)
        self.calc_model.command(key_text)
        self.main_display.setText(self.calc_model.get_display())

    def keyPressEvent(self, event):
        key_text = event.text()
        if key_text.isdigit() or key_text in "+-*/":
            self.calc_model.command(key_text)
            self.main_display.setText(self.calc_model.get_display())
        elif event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.calc_model.command("=")
            self.main_display.setText(self.calc_model.get_display())
        super().keyPressEvent(event)

    def __init__(self, title=None):
        super().__init__()
        self.setWindowTitle(title)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.main_display = QLabel('0')
        self.main_display.setAlignment(Qt.AlignRight)
        self.main_display.setFont(QFont("Times", 32))
        layout.addWidget(self.main_display)

        button_grid = QGridLayout()
        layout.addLayout(button_grid)

        buttons = (('AC', 'C', '?', '/'),
                   ('7', '8', '9', '*'),
                   ('4', '5', '6', '-'),
                   ('1', '2', '3', '+'),
                   ('0', '', '.', '='))

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

    def set_model(self, model):
        self.calc_model = model
        self.main_display.setText(model.get_display())


class AccountCalcViev(SimpleCalcView):
    def __init__(self, keys=None):
        super().__init__()
        keys_layout = QGridLayout()
        self.layout().addLayout(keys_layout)

        if keys is None:

            keys = (
                ('(', ')', '', '%'),
                ("MS", "MR", "MC", "M+", "M-")
            )



        for r in range(len(keys)):
            for c in range(len(keys[r])):
                key = keys[r][c]
                if key:
                    btn = QPushButton(text=key)
                    btn.clicked.connect(self.on_button_pressed)
                    keys_layout.addWidget(btn, r, c)
                    if key == '%':
                        keys_layout.addWidget(btn, r, c, 1, 2)

        def keyPressEvent(self, event):
            key_text = event.text()
            if key_text.isdigit() or key_text in "+-*/":
                self.calc_model.command(key_text)
                self.main_display.setText(self.calc_model.get_display())
            elif event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
                self.calc_model.command("=")
                self.main_display.setText(self.calc_model.get_display())
            super().keyPressEvent(event)


class MathCalcView(SimpleCalcView):

    def __init__(self,keys = None):
        super().__init__()
        keys_layout = QGridLayout()
        self.layout().addLayout(keys_layout)

        if keys is None:
            keys = (
                ('(', ')', 'log', 'x^2', 'x^3'),
                ("Sin", "Cos", "Tan", "ctg", "sqr")
            )

        for r in range(len(keys)):
            for c in range(len(keys[r])):
                key = keys[r][c]
                if key:
                    btn = QPushButton(text=key)
                    btn.clicked.connect(self.on_button_pressed)
                    keys_layout.addWidget(btn, r, c)
                    if key == '%':
                        keys_layout.addWidget(btn, r, c, 1, 2)


        def keyPressEvent(self, event):
            key_text = event.text()
            if key_text.isdigit() or key_text in "+-*/":
                self.calc_model.command(key_text)
                self.main_display.setText(self.calc_model.get_display())
            elif event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
                self.calc_model.command("=")
                self.main_display.setText(self.calc_model.get_display())
            super().keyPressEvent(event)