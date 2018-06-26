class IdentityOperators:

    def __init__(self, identity_operator, first_variable_to_compare, second_variable_to_compare):
        self.identity_operator = identity_operator
        self.first_variable_to_compare = first_variable_to_compare
        self.second_variable_to_compare = second_variable_to_compare
        self.identity_operators()

    def identity_operators(self):
        if self.identity_operator == "is":
            result = self.second_variable_to_compare is self.first_variable_to_compare
            identity_type = "'is': verify if {} is {} ".format(self.second_variable_to_compare,
                                                               self.first_variable_to_compare)
        elif self.identity_operator == "is not":
            result = self.second_variable_to_compare is not self.first_variable_to_compare
            identity_type = "'is not': verify if {} is not {} list".format(self.second_variable_to_compare,
                                                                           self.first_variable_to_compare)
        else:
            result = 'Error: This is not valid operator'
            identity_type = "?"

        print("Identity {}, with compare operator '{}' is {}"
              .format(identity_type, self.identity_operator, result))
