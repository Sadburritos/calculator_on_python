from math import sin, cos, tan, log, sqrt, pow
class SimpleCalcModel:
    _display = '0'

    def calculate(self):
        try:
            result = eval(self._display)
            self._display = str(result)
        except SyntaxError:
            print("Некорректное выражение")

    def command(self, key: str):
        if key != "=":
            if key.isdigit():
                if self._display == "0":
                    self._display = key
                else:
                    self._display += key
            else:
                if self._display[-1] not in "+-*/" and key in "+-*/":
                    self._display += key
            if key == "C":
                if len(self._display) > 0:
                    self._display = self._display[:-1]
            if key == "AC":
                self._display = "0"

        else:
            print(self._display)
            self.calculate()
        print(self._display, key)

    def get_display(self):
        return self._display

class AccountCalcModel(SimpleCalcModel):
    def __init__(self):
        super().__init__()
        self.calc_memory = ""

    def command(self, key: str):
        if key in "()":
            if self._display=="0":
                self._display=key
            else:
                self._display+=key
        if key == "%":
            last_value_index = max(self._display.rfind("-"),
                                   self._display.rfind("+"),
                                   self._display.rfind("*"),
                                   self._display.rfind("/"))
            if last_value_index < 0:
                return
            last_value = self._display[last_value_index:]
            self._display = self._display[:last_value_index]
            self.calculate()
            res1 = eval(f"{self._display}*{last_value}/100")
            self._display += str(res1)

        elif key == "MS":
            self.calc_memory = self._display
        elif key == "MR":
            if self.calc_memory == "":
                self._display = "0"
            else:
                self._display = self.calc_memory
        elif key == "MC":
            self.calc_memory = ""
        elif key == "M+":
            try:
                current_value = float(self._display)
                current_memory = float(self.calc_memory)
                self.calc_memory = str(current_memory + current_value)
                self._display = self.calc_memory
            except ValueError:
                self._display = "Error"
        elif key == "M-":
            try:
                current_value = float(self._display)
                current_memory = float(self.calc_memory)
                self.calc_memory = str(current_memory - current_value)
                self._display = self.calc_memory
            except ValueError:
                self._display = "Error"
        else:
            super().command(key)


class MathCalcModel(SimpleCalcModel):
    def __init(self):
        super().__init__()

    def command(self, key: str):
        if key in "()":
            if self._display=="0":
                self._display=key
            else:
                self._display+=key
        elif key == "Sin":
            self._display = str(sin(float(self._display)))
        elif key == "Cos":
            self._display = str(cos(float(self._display)))
        elif key == "Tan":
            self._display = str(tan(float(self._display)))
        elif key == "ctg":
            self._display = str(1.0 / tan(float(self._display)))
        elif key == "sqr":
            self._display = str(sqrt(float(self._display)))
        elif key == "x^2":
            self._display = str(pow(float(self._display), 2))
        elif key == "x^3":
            self._display = str(pow(float(self._display), 3))
        elif key == "log":
            try:
                value = float(self._display)
                if value > 0:
                    result = log(value)
                    self._display = str(result)
                else:
                    self._display = "Error: Value must be greater than 0"
            except ValueError:
                self._display = "Error: Invalid input"

        else:
            super().command(key)
if __name__ == '__main__':
    print('Testing model:')
    calc = AccountCalcModel()

    calc.command('3')
    calc.command('*')
    calc.command('7')
    calc.command('+')
    calc.command('1')
    calc.command('%')
    calc.command('')
    calc.calculate()

    print(calc.get_display())
