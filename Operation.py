class Operation:
    def __ini__(self, op1, op2, operator):
        self.op1 = op1
        self.op2 = op2
        self.operator = operator
    
    def calculate(self):
        if self.operator == '+':
            return self.op1 + self.op2
        elif self.operator == '-':
            return self.op1 - self.op2
        elif self.operator == '*':
            return self.op1 * self.op2
        elif self.operator == '/':
            if self.op2 == '0':
                raise ZeroDivisionError('No se puede dividir por cero')
            return self.op1 / self.op2
        else:
            raise ValueError('Operador no valido')
    