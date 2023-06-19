class Calculator:
    def __init__(self):
        pass

    def addition(self, int1, int2):
        return int1 + int2

    def subtraction(self, int1, int2):
        return int1 - int2

    def multiplication(self, int1, int2):
        return int1 * int2

    def division(self, int1, int2):
        if int2 != 0:
            return int1 / int2
        else:
            return "Error"

    def modulus(self, int1, int2):
        return int1 % int2


# Usage example:
calc = Calculator()
result_add = calc.addition(7, 3)
print("addition:", result_add)

result_sub = calc.subtraction(7, 3)
print("subtraction:", result_sub)

result_mul = calc.multiplication(7, 3)
print("multiplication:", result_mul)

result_div = calc.division(7, 3)
print("division:", result_div)

result_mod = calc.modulus(7, 3)
print("modulus:", result_mod)
