from OmarHuanca.python.exam.Employee import Employee
from OmarHuanca.python.exam.calculator.ProductionSalary import ProductionSalary


class ProductionEmployee(Employee):
    def __init__(self, name, effective_pieces, defective_pieces, department, num):
        super().__init__(name, effective_pieces)
        self.defective_pieces = defective_pieces
        self.department = department
        self.id = "PE_" + str(num)
        self.salary_calculator = ProductionSalary(self.effective_pieces, self.defective_pieces)
        self.logger.info("Production Employee Created: {}".format(self.name))

    def __str__(self):
        print("====== Commercial Employee Information =======")
        data = ["ID: {}".format(self.id),
                "Name: {}".format(self.name),
                "Departament: {}".format(self.department),
                "Salary: {}".format(self.get_salary()),
                "Discount: {}".format(self.get_discount()),
                "Total Salary: {}".format(self.get_total_salary())]
        return '\n'.join(data)

    def get_departament(self):
        return self.department

    def get_id(self):
        return self.id

    def get_salary(self):
        return self.salary_calculator.get_salary()

    def get_discount(self):
        return self.salary_calculator.get_discount()

    def get_total_salary(self):
        return self.salary_calculator.get_net_salary()


if __name__ == "__main__":
    production_employee = ProductionEmployee("Production Employee", 2, 2, "Production", 21)
    print(production_employee)
