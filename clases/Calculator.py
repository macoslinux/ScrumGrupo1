from clases.PostFixEvaluator import PostFixEvaluator

class Calculator:
    def __init__(self):
        self.evaluator = PostFixEvaluator()

    def process_expresion(self, expression):
        try:
            self.evaluator.is_valid_postfix_expression(expression)
            result = self.evaluator.evaluate_expression(expression)
            self.show_result(result)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    def show_result(self, result):
        print(f"Resultado: {result}")
