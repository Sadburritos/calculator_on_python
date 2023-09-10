from PyQt5.QtWidgets import *

class CalcMainWindow(QMainWindow):
    calc_view = None
    calc_layout = None

    def __init__(self, title):
        super().__init__()
        self.calc_model = None
        self.setStyleSheet("background-color: black;")
        self.setWindowTitle(title)
        main_widget = QWidget()
        self.calc_layout = QGridLayout()
        main_widget.setLayout(self.calc_layout)
        self.setCentralWidget(main_widget)

    def set_view(self, view):
        self.calc_view = view
        self.calc_layout.addWidget(self.calc_view, 1, 0)

    def set_model(self, model):
        self.calc_model = model
        if self.calc_view:
            self.calc_view.set_model(model)

    def set_switcher(self, widget):
        self.calc_layout.addWidget(widget, 0, 0)
