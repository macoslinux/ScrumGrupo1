from clases.Operation import Operation

class PostFixEvaluator:
    def __init__(self):
        self.operators = {'+', '-', '*', '/'}
    
    def is_operator(self, operator):
        return operator in self.operators
    
    def is_valid_postfix_expression(self, postfix_expression):
        stack = 0

        for token in postfix_expression.split():
            if token not in self.operators:
                stack += 1
            else:
                if stack < 2:
                    return False
                stack -= 1
        return stack == 1

    def evaluate_expression(self, postfix_expression):
        stack = []
        
        for token in postfix_expression.split():
            if token.isdigit() or (token[1:].isdigit() and token[0] == '-'):  # Si es un número
                stack.append(float(token))
            elif self.is_operator(token):  # Si es un operador
                try:
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    # Usamos la clase Operacion para resolver la operación
                    operation = Operation(operand1, operand2, token)
                    result = operation.calculate()  # Resolvemos con la clase Operacion
                    stack.append(result)
                except IndexError:
                    raise ValueError("Expresión postfija incorrecta")
            #else:
            #    raise ValueError(f"Token no válido: {token}")
        
        if len(stack) != 1:
            raise ValueError("Expresión postfija incorrecta")
        
        return stack.pop()
