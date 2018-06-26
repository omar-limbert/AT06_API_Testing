class AssignmentOperators:

    def __init__(self, compare_operator, first_variable_to_assign, second_variable_to_assign):
        self.compare_operator = compare_operator
        self.first_variable_to_assign = first_variable_to_assign
        self.second_variable_to_assign = second_variable_to_assign
        self.assignment_operators()

    def assignment_operators(self):
        if self.compare_operator == "=":
            result = self.first_variable_to_assign + self.second_variable_to_assign
            assignment_type = "Assigns Values C = {} + {} the value into C".format(self.first_variable_to_assign,
                                                                                   self.second_variable_to_assign)
        elif self.compare_operator == "+=":
            assignment_type = "+= Add AND, {} += {},".format(self.first_variable_to_assign,
                                                             self.second_variable_to_assign)
            self.first_variable_to_assign += self.second_variable_to_assign
            result = self.first_variable_to_assign

        elif self.compare_operator == "-=":
            assignment_type = "-= Subtract AND, {} -= {},".format(self.first_variable_to_assign,
                                                                  self.second_variable_to_assign)
            self.first_variable_to_assign -= self.second_variable_to_assign
            result = self.first_variable_to_assign

        elif self.compare_operator == "*=":
            assignment_type = "*= Multiply AND, {} *= {},".format(self.first_variable_to_assign,
                                                                  self.second_variable_to_assign)
            self.first_variable_to_assign *= self.second_variable_to_assign
            result = self.first_variable_to_assign

        elif self.compare_operator == "/=":
            assignment_type = "/= Divide AND, {} /= {},".format(self.first_variable_to_assign,
                                                                self.second_variable_to_assign)
            self.first_variable_to_assign /= self.second_variable_to_assign
            result = self.first_variable_to_assign

        elif self.compare_operator == "%=":
            assignment_type = "%= Multiply AND, {} %= {},".format(self.first_variable_to_assign,
                                                                  self.second_variable_to_assign)
            self.first_variable_to_assign %= self.second_variable_to_assign
            result = self.first_variable_to_assign

        else:
            result = 'Error: This is not valid operator'
            assignment_type = "?"

        print("Result of {} with compare operator '{}' is {}"
              .format(assignment_type, self.compare_operator, result))
