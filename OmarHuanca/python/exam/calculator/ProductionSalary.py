from OmarHuanca.python.exam.calculator.Salary import Salary


class ProductionSalary(Salary):

    def __init__(self, effective_pieces, defective_pieces):
        super().__init__(effective_pieces)
        self.defective_pieces = defective_pieces

    def get_salary(self):
        self.logger.info("Get Production Salary")
        return (self.defective_pieces * 10) + (self.defective_pieces * 1.3)

    def get_discount(self):
        self.logger.info("Get Production Discount")
        return self.get_salary() * 12.5 / 100

    def get_net_salary(self):
        self.logger.info("Get Production Net Salary")
        return self.get_salary() - self.get_discount()
