class Operation:
    def __init__(self, operand1, operand2, operator):
        self.operand1 = operand1
        self.operand2 = operand2
        self.operator = operator

    def calculate(self):
        if self.operator == "+":
            return self.operand1 + self.operand2
        elif self.operator == "-":
            return self.operand1 - self.operand2
        elif self.operator == "*":
            return self.operand1 * self.operand2
        elif self.operator == "/":
            if self.operand2 == 0:
                raise ZeroDivisionError("No se puede dividir por cero")
            return self.operand1 / self.operand2
        else:
            raise ValueError(f"Operador no válido '{self.operator}' ")

    def get_operation(self):
        return f"{self.operand1} {self.operator} {self.operand2}"
