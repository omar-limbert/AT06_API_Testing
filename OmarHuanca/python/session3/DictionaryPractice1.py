dictionary_global = {}


class DictionaryPractice1:

    @classmethod
    def fill_dictionary(cls):
        number_of_elements = int(cls.read_length_of_dictionary())
        global dictionary_global
        for i in range(1, number_of_elements + 1):
            key_to_insert = cls.read_and_verify_is_key_exists()
            value_to_insert = cls.read_and_verify_is_value_exists()
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
    def read_and_verify_is_key_exists(cls):
        while True:
            key_to_verify = input("Insert Key: ")
            if cls.is_key_inserted_exists(key_to_verify):
                print("The key [{}] already exists, try again".format(key_to_verify))
            else:
                return key_to_verify

    @classmethod
    def read_and_verify_is_value_exists(cls):
        while True:
            value_to_verify = input("Insert Value: ")
            if cls.is_value_inserted_exists(value_to_verify):
                print("The value [{}] already exists, try again".format(value_to_verify))
            else:
                return value_to_verify

    @classmethod
    def print_the_dictionary_keys(cls):
        print(dictionary_global.keys())

    @classmethod
    def print_the_dictionary_values(cls):
        print(dictionary_global.values())

    @classmethod
    def print_the_dictionary(cls):
        print(dictionary_global)

    @classmethod
    def is_key_inserted_exists(cls, key):
        return key in dictionary_global.keys()

    @classmethod
    def is_value_inserted_exists(cls, key):
        return key in dictionary_global.values()

    @classmethod
    def run_practice_one(cls):
        print("PRACTICE 1")
        cls.fill_dictionary()
        print("=> Function to print the dictionary keys")
        cls.print_the_dictionary_keys()
        print("=> Function to print the dictionary values")
        cls.print_the_dictionary_values()
        print("=> Function to print the dictionary")
        cls.print_the_dictionary()
        print("=> Function to define is a key inserted by the user, exists on the dictionary.")
        cls.read_and_verify_is_key_exists()
        print("=> Function to define is a value inserted by the user, exists on the dictionary.")
        cls.read_and_verify_is_value_exists()


script = DictionaryPractice1
script.run_practice_one()
