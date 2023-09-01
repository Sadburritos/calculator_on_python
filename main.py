import sys
from PyQt5.QtWidgets import *
from calc_main_window import *
from calc_view import *
from calc_model import *


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = CalcMainWindow('Qalculus v. 1.0')
    view = SimpleCalcView()
    model = SimpleCalcModel()
    view.set_model(model)
    window.set_view(view)
    window.show()
    app.exec()

