from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class My_calculator(QWidget):
    def __init__(self, title):
        super().__init__()
        self.setStyleSheet("background-color: black;")
        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle(title)

        self.buttons()

    def buttons(self):
        layout = QVBoxLayout()

        button_mode_layout = QHBoxLayout()
        normal_button = QPushButton('Normal')
        normal_button.setStyleSheet("background-color : yellow")
        math_button = QPushButton('Math')
        math_button.setStyleSheet("background-color : red")
        acc_button = QPushButton('Acc')
        acc_button.setStyleSheet("background-color : pink")
        button_mode_layout.addWidget(normal_button)
        button_mode_layout.addWidget(math_button)
        button_mode_layout.addWidget(acc_button)
        layout.addLayout(button_mode_layout)

        self.result_label = QLabel('0')
        self.result_label.setAlignment(Qt.AlignRight)
        self.result_label.setStyleSheet('color: rgb(255, 255, 255)')
        self.result_label.setFont(QFont("Times", 32))
        layout.addWidget(self.result_label)

        button_grid = QGridLayout()

        buttons = [
            'C', 'AC', '', '',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row, col = 0, 0
        for nums in buttons:
            button = QPushButton(nums)
            button_grid.addWidget(button, row, col)
            button.setStyleSheet("background-color : orange")

            col += 1
            if col > 3:
                col = 0
                row += 1

        layout.addLayout(button_grid)

        self.setLayout(layout)



def main():
    app = QApplication([])
    calculator = My_calculator()
    calculator.show()
    app.exec_()


if __name__ == "__main__":
    main()
