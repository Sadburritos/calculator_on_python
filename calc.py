from PyQt5.QtWidgets import *

# я перешел на пайчарм может быть чтото будет не так


class My_calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 100, 300)

        self.buttons()

    def buttons(self):
        layout = QVBoxLayout()

        self.result_label = QLabel('0')
        layout.addWidget(self.result_label)

        button_grid = QGridLayout()
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row, col = 0, 0
        for nums in buttons:
            button = QPushButton(nums)
            button_grid.addWidget(button, row, col)

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


main()

