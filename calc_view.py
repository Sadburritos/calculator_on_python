from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

BUTTON_SIZE = 50  # Размер кнопок

class My_calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 400)
        self.current_input = ''
        self.result = 0

        layout = QVBoxLayout()

        button_mode_layout = QHBoxLayout()
        normal_button = QPushButton('Normal')
        math_button = QPushButton('Math')
        acc_button = QPushButton('Acc')
        button_mode_layout.addWidget(normal_button)
        button_mode_layout.addWidget(math_button)
        button_mode_layout.addWidget(acc_button)
        layout.addLayout(button_mode_layout)

        self.result_label = QLabel('0')
        self.result_label.setAlignment(Qt.AlignRight)
        self.result_label.setFont(QFont("Times", 32))
        layout.addWidget(self.result_label)

        button_grid = self._createButtons()
        layout.addLayout(button_grid)

        self.setLayout(layout)

    def _createButtons(self):
        self.buttonMap = {}
        buttonsLayout = QGridLayout()
        keyBoard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]

        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttonsLayout.addWidget(self.buttonMap[key], row, col)

                # Добавьте обработчик события для каждой кнопки
                self.buttonMap[key].clicked.connect(self.button_click)

        return buttonsLayout

    def button_click(self):
        sender = self.sender()  # Получить отправителя события (кнопку)
        if sender:
            button_text = sender.text()  # Получить текст кнопки

            if button_text == '=':
                try:
                    # Выполните вычисления и обновите результат
                    result = eval(self.current_input)
                    self.result = result
                    self.current_input = str(result)
                    self.result_label.setText(self.current_input)
                except Exception as e:
                    self.result_label.setText('Error')
                    self.current_input = ''
            elif button_text == 'C':
                # Очистите текущий ввод
                self.current_input = ''
                self.result_label.setText('0')
            else:
                # Добавьте текст кнопки к текущему вводу
                self.current_input += button_text
                self.result_label.setText(self.current_input)

    def set_model(self,model):
        self.calc_model = model
        self.main_display.setText(model.get_display())


class AccountCalcViev(SimpleCalcView):
    def __init__(self):
        super().__init__()
        keys_layout = QGridLayout()
        self.layout().addLayout(keys_layout)

        keys = ('(', ')', '%', '')

        for r in range(len(keys)):
            key = keys[r]
            if key:
                btn = QPushButton(text=key)
                btn.clicked.connect(self.on_button_pressed)
                if key != '%':
                    keys_layout.addWidget(btn, 0, r)
                else:
                    keys_layout.addWidget(btn, 0, r, 1, 2)

