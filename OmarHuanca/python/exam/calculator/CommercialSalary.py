from OmarHuanca.python.exam.calculator.Salary import Salary


class CommercialSalary(Salary):

    def __init__(self, effective_pieces):
        super().__init__(effective_pieces)

    def get_salary(self):
        self.logger.info("Get Commercial Salary")
        return self.effective_pieces * 2.5

    def get_discount(self):
        self.logger.info("Get Commercial Discount")
        return self.get_salary() * 12.5 / 100

    def get_net_salary(self):
        self.logger.info("Get Commercial Net Salary")
        return self.get_salary() - self.get_discount()
