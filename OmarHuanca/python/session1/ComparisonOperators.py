class ComparisonOperators:

    def __init__(self, compare_operator, first_variable_to_compare, second_variable_to_compare):
        self.compare_operator = compare_operator
        self.first_variable_to_compare = first_variable_to_compare
        self.second_variable_to_compare = second_variable_to_compare
        self.comparison_operators()

    def comparison_operators(self):
        if self.compare_operator == "==":
            result = self.first_variable_to_compare == self.second_variable_to_compare
            comparison_type = "Equal"

        elif self.compare_operator == "!=":
            result = self.first_variable_to_compare != self.second_variable_to_compare
            comparison_type = "Not Equal"

        elif self.compare_operator == ">":
            result = self.first_variable_to_compare > self.second_variable_to_compare
            comparison_type = "Is Greater That"

        elif self.compare_operator == "<":
            result = self.first_variable_to_compare < self.second_variable_to_compare
            comparison_type = "Is Less That"

        elif self.compare_operator == ">=":
            result = self.first_variable_to_compare >= self.second_variable_to_compare
            comparison_type = "Is Greater Or Equal That"

        elif self.compare_operator == "<=":
            result = self.first_variable_to_compare <= self.second_variable_to_compare
            comparison_type = "Is Less Or Equal That"

        else:
            result = 'Error: This is not valid operator'
            comparison_type = "?"

        print("Result of {}: {} {} {} = {}"
              .format(comparison_type,
                      self.first_variable_to_compare,
                      self.compare_operator,
                      self.second_variable_to_compare, result))
