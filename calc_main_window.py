from PyQt5.QtWidgets import QMainWindow

class CalcMainWindow(QMainWindow):
    calc_view = None
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)

    def set_view(self, view):
        self.calc_view = view
        self.setCentralWidget(self.calc_view)
