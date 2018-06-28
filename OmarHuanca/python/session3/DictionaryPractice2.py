from OmarHuanca.python.session2.PrimeNumber import PrimeNumber

dictionary_global = {}


class DictionaryPractice2:

    @classmethod
    def fill_dictionary(cls):
        number_of_elements = int(cls.read_length_of_dictionary())
        global dictionary_global
        for i in range(1, number_of_elements + 1):
            key_to_insert = cls.read_and_verify_key()
            value_to_insert = key_to_insert ** 2
            dictionary_global.update({key_to_insert: value_to_insert})

    @classmethod
    def read_length_of_dictionary(cls):
        while True:
            try:
                return int(input('How many elements you will insert into dictionary?: '))
            except ValueError:
                print("Is not valid number, please try again.")
                pass

    @classmethod
    def read_and_verify_key(cls):
        while True:
            try:
                key_to_verify = int(input("Insert Key [number value (1 to 9)] : "))
                if 0 < key_to_verify <= 9:
                    return key_to_verify
                else:
                    print("The number value must be 1 to 9, try again")
                    pass
            except ValueError:
                print("Is not valid number, please try again.")
                pass

    @classmethod
    def prime_numbers_of_dictionary(cls):
        prime_number = PrimeNumber

        for key in list(dictionary_global.keys()):
            if not prime_number.is_prime(dictionary_global.get(key) and prime_number.is_prime(key)):
                del dictionary_global[key]

    @classmethod
    def print_the_dictionary(cls):
        print(dictionary_global)

    @classmethod
    def run_practice_two(cls):
        print("PRACTICE 2")
        cls.fill_dictionary()
        print("=> Define a function that can return a dictionary where "
              "the keys are numbers between 1 and 9 "
              "(both included) and the values are square of keys.")
        print("Answer: Dictionary with square values")
        cls.print_the_dictionary()
        print("Define a function to print a dictionary that contains "
              "all the prime numbers extracted from the previous dictionary.")
        cls.prime_numbers_of_dictionary()
        print("Answer: Dictionary with prime keys and values")
        cls.print_the_dictionary()


script = DictionaryPractice2
script.run_practice_two()
