from OmarHuanca.python.session4.practice_1.age_module import age_module, validate_age_module

dictionary_global = {}


class ShowAge:

    @classmethod
    def fill_dictionary(cls):
        number_of_users = int(cls.read_length_of_dictionary())
        global dictionary_global
        for i in range(1, number_of_users + 1):
            key_to_insert = input("[{}] - Please enter a Name of User: ".format(i))
            value_to_insert = input("[{}] - Please enter a Age of User: ".format(i))
            dictionary_global.update({key_to_insert: value_to_insert})

    @classmethod
    def read_length_of_dictionary(cls):
        while True:
            try:
                return int(input('How many Users do you need add? : '))
            except ValueError:
                print("Is not valid number, please try again.")
                pass

    @classmethod
    def show_dictionary_with_ages(cls):
        for key in dictionary_global:
            age = int(dictionary_global[key])
            print(key, age_module.get_age_in_days(21))
            print("[{}]-[{}] - Age: {} years old, Ages[{} days, {} hours, {} minutes.]".format(
                validate_age_module.validate_age(age),
                key,
                age,
                age_module.get_age_in_days(age),
                age_module.get_age_in_hours(age),
                age_module.get_age_in_minutes(age)))

    @classmethod
    def run_practice_one(cls):
        print("[MODULES] - PRACTICE 1")
        cls.fill_dictionary()
        cls.show_dictionary_with_ages()


script = ShowAge
script.run_practice_one()
