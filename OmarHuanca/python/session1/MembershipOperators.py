class MembershipOperators:

    def __init__(self, compare_operator, variable_list, variable_to_find):
        self.compare_operator = compare_operator
        self.variable_list = variable_list
        self.variable_to_find = variable_to_find
        self.membership_operators()

    def membership_operators(self):
        if self.compare_operator == "in":
            result = self.variable_to_find in self.variable_list
            membership_type = "'in': verify if {} into {} list".format(self.variable_to_find,
                                                                       self.variable_list)
        elif self.compare_operator == "not in":
            result = self.variable_to_find not in self.variable_list
            membership_type = "'not in': verify if {} not into {} list".format(self.variable_to_find,
                                                                               self.variable_list)
        else:
            result = 'Error: This is not valid operator'
            membership_type = "?"

        print("Membership {}, with compare operator '{}' is {}"
              .format(membership_type, self.compare_operator, result))
