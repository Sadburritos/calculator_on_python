import sys
import os
from calc_main_window import *
from calc_view import *
from calc_model import *
from calc_control import *


def switch_mode(name):
    global view
    if name == "ACC":
        model = AccountCalcModel()
        view.hide()
        view = AccountCalcViev()
        view.set_model(model)
        window.set_view(view)

    if name == "Default":
        model = SimpleCalcModel()
        view.hide()
        view = SimpleCalcView()
        view.set_model(model)
        window.set_view(view)


if __name__ == '__main__':
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "venv/Lib/site-packages/PyQt5/Qt5/plugins/platforms"

    app = QApplication(sys.argv)

    window = CalcMainWindow('Calculator')
    model = SimpleCalcModel()
    view = SimpleCalcView()

    switch = CalcControlWidget()
    switch.switched.connect(switch_mode)
    window.set_switcher(switch)

    view.set_model(model)
    window.set_view(view)
    window.show()

    app.exec_()
