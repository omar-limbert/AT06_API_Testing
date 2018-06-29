from OmarHuanca.python.session4.practice_2.circle_module import area_module
from OmarHuanca.python.session4.practice_2.circle_module import perimeter_module


class ShowRadius:

    @classmethod
    def read_radius_from_user(cls):
        while True:
            try:
                return int(input('Please insert radius of your circle : '))
            except ValueError:
                print("Is not valid number, please try again.")
                pass

    @classmethod
    def show_circle_information(cls, radius):
        print("Circle Information...")
        print("Area of Circle: [{}]".format(area_module.area_of_circle(radius)))
        print("Perimeter of Circle: [{}]".format(perimeter_module.perimeter_of_circle(radius)))

    @classmethod
    def run_practice_two(cls):
        print("[CIRCLE] - PRACTICE 2")
        radius = cls.read_radius_from_user()
        cls.show_circle_information(radius)


script = ShowRadius
script.run_practice_two()
