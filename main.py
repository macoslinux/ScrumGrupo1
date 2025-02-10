from clases.Calculator import Calculator
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def read_key():
    input('\nPresiona cualquier tecla para continuar...')

def menu():
    print('***************************************************************************')
    print('                     ELIJA UNA OPCION PARA EJECUTAR')
    print('***************************************************************************')
    print('\n[A] - Resolver operacion aritmetica (+, -, *, /) ')
    #print('[E] - Resolver ecuaciones de primer grado dado dos variables con sus valores')
    #print('[S] - Simplificar ecuaciones al tener varias variables')
    print('[X] - Salir')

def main():
    opcion = None
    
    while opcion != 'X':
        clear()
        menu()
        opcion = input('\nOpcion: ').upper()
        
        if opcion == 'A':
            expresion = input('Ingrese una expresion aritmetica en notacion postfija (ej. 2 2 +) para resolver:\n')
            solve_expression(expresion)
            read_key()

def solve_expression(expression):
    calculator = Calculator()
    calculator.process_expresion(expression)


if __name__ == '__main__':
    main()