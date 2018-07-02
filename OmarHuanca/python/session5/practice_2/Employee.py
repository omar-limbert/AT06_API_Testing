from OmarHuanca.python.session5.practice_2.Person import Person


class Employee(Person):

    def __init__(self, name, last_name, age, ci, employee_id):
        super().__init__(name, last_name, age, ci)
        self.employee_id = employee_id

    def __str__(self):
        print("====== Employee Information =======")
        rows = ["ID: {}".format(self.employee_id),
                "CI: {}".format(self.ci),
                "Name: {}".format(self.name),
                "Last Name: {}".format(self.last_name),
                "Age: {}".format(self.age)]
        return '\n'.join(rows)


if __name__ == "__main__":
    script = Employee("employee", "employe last name", "25", "3454313", "1")
print(script)
