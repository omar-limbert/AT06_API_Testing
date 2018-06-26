class PerformOperation:

    def __init__(self, arithmetic_operator, number_a, number_b):
        self.arithmetic_operator = arithmetic_operator
        self.number_a = int(number_a)
        self.number_b = int(number_b)
        self.arithmetic_operators()

    def arithmetic_operators(self):
        if self.arithmetic_operator == "+":
            result = self.number_a + self.number_b
            arithmetic_type = "Addition"

        elif self.arithmetic_operator == "-":
            result = self.number_a - self.number_b
            arithmetic_type = "Subtraction"

        elif self.arithmetic_operator == "*":
            result = self.number_a * self.number_b
            arithmetic_type = "Multiplication"

        elif self.arithmetic_operator == "/":
            result = self.number_a / self.number_b
            arithmetic_type = "Division"

        elif self.arithmetic_operator == "%":
            result = self.number_a % self.number_b
            arithmetic_type = "Modulus"

        elif self.arithmetic_operator == "**":
            result = self.number_a ** self.number_b
            arithmetic_type = "Exponent"

        elif self.arithmetic_operator == "//":
            result = self.number_a // self.number_b
            arithmetic_type = "Floor Division"

        else:
            result = 'Error: This is not valid operator'
            arithmetic_type = "?"

        print("Result of {}: {} {} {} = {}".format(arithmetic_type,
                                                   self.number_a,
                                                   self.arithmetic_operator,
                                                   self.number_b, result))
