import re

from OmarHuanca.SingletonLogger import SingletonLogger
from OmarHuanca.python.exam.CommercialEmployee import CommercialEmployee
from OmarHuanca.python.exam.ProductionEmployee import ProductionEmployee


class MainMenu:

    def __init__(self):
        self.logger = SingletonLogger.__call__().get_logger()
        self.employee_list = []

    def __str__(self):
        rows = []
        print("List Of Employee(s): [{}] registered".format(len(self.employee_list)))
        print("Employee ID | Name  | Departament | Global Salary | Total Discount | Net Salary ")
        for employee in self.employee_list:
            rows.append("{} | {} | {} | {} | {} | {}".format(employee.get_id(), employee.get_name(), employee.get_departament(), employee.get_salary(), employee.get_discount(), employee.get_total_salary()))
        return '\n'.join(rows)

    def fill_employee_list(self):
        self.logger.info("Fill Employee List")
        number_of_elements = int(self.read_length_of_employee_list())
        for i in range(1, number_of_elements + 1):
            employee = self.fill_employee_information(i)
            self.employee_list.append(employee)

    def fill_employee_information(self, index):
        print("Employe [{}]".format(index))
        employee_name = input('Insert Name of Employee: ')
        if self.read_departament() == 1:
            departament = "Commercial"
        else:
            departament = "Production"
        effective_pieces = self.read_effective_pieces()

        if departament == "Commercial":
            return CommercialEmployee(employee_name, effective_pieces, departament, index)
        else:
            defective_pieces = self.read_defective_pieces()
            return ProductionEmployee(employee_name, effective_pieces, defective_pieces, departament, index)

    def read_defective_pieces(self):
        while True:
            try:
                return int(input('Enter Defective Pieces: '))
            except ValueError:
                print("Is not valid number, please try again.")
                pass

    def read_effective_pieces(self):
        while True:
            try:
                return int(input('Enter Effective Pieces: '))
            except ValueError:
                print("Is not valid number, please try again.")
                pass

    def read_departament(self):
        while True:
            print("Choose one departament")
            print("(1) Commercial")
            print("(2) Production")
            try:
                departament = int(input('Enter Option: '))
                if self.is_valid_departament(departament):
                    return departament
                else:
                    print("come on..!")
                    pass
            except ValueError:
                print("Is not valid number, please try again.")
                pass

    def read_length_of_employee_list(self):
        while True:
            try:
                size_of_list = int(input('How many [Employee(s)] you will insert into List? (3-15) '))
                if self.is_valid_length_of_list(size_of_list):
                    return size_of_list
                else:
                    print("[Please insert value no less than 3 and no more than 15]")
                    pass
            except ValueError:
                print("Is not valid number, please try again.")
                pass

    def is_valid_departament(self, departament):
        return re.fullmatch("[1-2]", str(departament))

    def is_valid_length_of_list(self, id_to_verify):
        return id_to_verify in range(3, 15)

    def show_employee_list(self):
        for employee in self.employee_list:
            print(employee.get_name())


if __name__ == "__main__":
    shop = MainMenu()
    shop.fill_employee_list()
    print(shop)
