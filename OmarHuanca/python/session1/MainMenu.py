import sys

from OmarHuanca.python.session1.AssignmentOperators import AssignmentOperators
from OmarHuanca.python.session1.ComparisonOperators import ComparisonOperators
from OmarHuanca.python.session1.IdentityOperators import IdentityOperators
from OmarHuanca.python.session1.MembershipOperators import MembershipOperators
from OmarHuanca.python.session1.PerformOperation import PerformOperation


class MainMenu:

    def __init__(self):

        self.main_menu()

    def main_menu(self):

        while True:
            print("=========================================================")
            print("Welcome to Python Operators - Samples")
            print("=========================================================")
            print("(1) - Arithmetic's Operators")
            print("(2) - Comparison Operators")
            print("(3) - Assignment Operators")
            print("(4) - Membership Operators")
            print("(5) - Identity Operators")
            print("(6) - Practice")
            print("(7) - Exit")

            try:
                option = input('Enter your option: ')
            except SyntaxError:
                option = 0
                pass

            if option is "1":
                self.perform_operation()
            elif option is "2":
                self.comparison_operators()
            elif option is "3":
                self.assignment_operators()
            elif option is "4":
                self.membership_operators()
            elif option is "5":
                self.identity_operators()
            elif option is "6":
                self.practice_operator()
            elif option is "7":
                sys.exit()

    def perform_operation(self):

        PerformOperation("+", 2, 2)
        PerformOperation("-", 2, 1)
        PerformOperation("*", 2, 1)
        PerformOperation("/", 2, 1)
        PerformOperation("%", 2, 1)
        PerformOperation("**", 2, 2)
        PerformOperation("//", -11, 3)
        PerformOperation("++", 2, 1)

    def comparison_operators(self):

        ComparisonOperators("==", "a", "b")
        ComparisonOperators("!=", "a", "b")
        ComparisonOperators(">", 2, 1)
        ComparisonOperators("<", 2, 1)
        ComparisonOperators(">=", 2, 1)
        ComparisonOperators("<=", 2, 2)
        ComparisonOperators(">>=", 2, 1)

    def assignment_operators(self):

        AssignmentOperators("=", 1, 2)
        AssignmentOperators("+=", 2, 2)
        AssignmentOperators("-=", 2, 2)
        AssignmentOperators("*=", 2, 2)
        AssignmentOperators("/=", 2, 2)
        AssignmentOperators("%=", 2, 2)
        AssignmentOperators("/==", 2, 1)

    def membership_operators(self):

        MembershipOperators("in", [1, 2, 3, 4, 5, 6, 7], 4)
        MembershipOperators("in", ["a", "b", "c", "d"], "b")
        MembershipOperators("not in", [1, 2, 3, 4, 5, 6, 7], 0)
        MembershipOperators("not in", ["a", "b", "c", "d"], "E")
        MembershipOperators("is in", ["a", "b", "c", "d"], "E")

    def identity_operators(self):

        IdentityOperators("is", 4, 4)
        IdentityOperators("is", "a", "a")
        IdentityOperators("is not", 5, 6)
        IdentityOperators("is not", "B", "b")
        IdentityOperators("is in", 1, 1)

    def practice_operator(self):

        print("=========================================================")
        print("Please select Operator to practice ")
        print("(1) - Arithmetic's Operators")
        print("(2) - Comparison Operators")
        print("(3) - Assignment Operators")
        print("(4) - Membership Operators")
        print("(5) - Identity Operators")

        try:
            practice_option = input('Enter your option: ')
        except SyntaxError:
            pass

        if practice_option is "1":
            operator = input("Insert Operator: + , - , * , / , % , ** , // : ")
            first_value = input("Insert first number value: ")
            second_value = input("Insert second number value: ")
            PerformOperation(operator, first_value, second_value)
        elif practice_option is "2":
            operator = input("Insert Operator: == , != , > , < , >= , <= : ")
            first_value = input("Insert first value: ")
            second_value = input("Insert second value: ")
            ComparisonOperators(operator, first_value, second_value)
        elif practice_option is "3":
            operator = input("Insert Operator: = , += ,  -= , *= , /= , %= : ")
            first_value = input("Insert first value: ")
            second_value = input("Insert second value: ")
            AssignmentOperators(operator, first_value, second_value)
        elif practice_option is "4":
            operator = input("Insert Operator: 'in' , 'not in' : ")
            first_value = input("Insert list e.g. '[1,2,3,4,5,]': ")
            second_value = input("Insert value to find on list before ")
            MembershipOperators(operator, first_value, second_value)
        elif practice_option is "5":
            operator = input("Insert Operator: 'is' , 'is not' : ")
            first_value = input("Insert first value: ")
            second_value = input("Insert second value: ")
            IdentityOperators(operator, first_value, second_value)
        elif practice_option is "7":
            pass


script = MainMenu()
