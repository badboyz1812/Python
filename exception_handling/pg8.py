def division(dividend,divisor):
    try:
        result = dividend/divisor
        print("result",result)
    except ArithmeticError:
        print("Error:Arithmetic error occured")

dividend = float(input('Enter the value of dividend '))
divisor = float(input('Enter the value of divisor '))

division(dividend,divisor)