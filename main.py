import sys
from PyQt5.QtWidgets import QApplication
from calc_main_window import CalcMainWindow
from calc_view import My_calculator

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = CalcMainWindow('Calculator')
    view = My_calculator()

    window.set_view(view)
    window.show()
    app.exec_()
