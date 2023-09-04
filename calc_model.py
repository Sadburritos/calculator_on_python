
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class SimpleCalcModel:
    _display = '0'

    def calculate(self):
        try:
            result = eval(self._display)
            self._display = str(result)
        except SyntaxError:
            print("Некоректное выражение")

    def command(self, key: str):
        if key != "=": 
            if key.isdigit():
                if self._display == "0":
                    self._display = key
                else: 
                    self._display += key
            else: 
                if self._display[-1] not in "+-*/":
                    self._display += key
            
            if key == "C": 
                if len(self._display) > 1:
                    self._display = self._display[:-1]

            if key == "AC":
                self._display = "0"
        else: 
            print(self._display)
            self.calculate() 

    def get_display(self):
        return self._display

# class AcccountCalcmodel(SimpleCalcModel):
#     def command(self,key:str):
#         if key in '()':
#             self._display += key
#         elif key == "%": # 3*7-1 => "3*7", "-1"
#             last_value_index = max(self._display.rfind("-"),
#                                    self._display.rfind("+"),
#                                    self._display.rfind("/"),
#                                    self._display.rfind("*"))
#             if last_value_index < 0 :
#                 return
#             last_value = self._display[last_value_index:]
#             self._display = self._display[:last_value_index]
#             self.calculate()
#             # result = float(self._display) / 100
#             res1 = eval(f"{self._display} * {last_value}/100")
#             self._display += res1
#         else:
#             super().command(key)
if __name__ == '__main__':
    print('Testing model:')
    calc = SimpleCalcModel()

    calc.command('3')
    calc.command('*')
    calc.command('7')
    calc.command('-')
    calc.command('1')
    calc.command('=')
    calc.calculate()

    print(calc.get_display())
