import re

dictionary_global = {}


class UserManager:

    @classmethod
    def fill_dictionary(cls):
        number_of_elements = int(cls.read_length_of_dictionary())
        global dictionary_global
        for i in range(1, number_of_elements + 1):
            user_id = cls.read_and_verify_user_id()
            user_name = cls.read_and_verify_user_name()
            dictionary_global.update({user_id: user_name})

    @classmethod
    def read_length_of_dictionary(cls):
        while True:
            try:
                return int(input('How many [Users] you will insert into dictionary?: '))
            except ValueError:
                print("Is not valid number, please try again.")
                pass

    @classmethod
    def read_and_verify_user_id(cls):
        while True:
            key_to_verify = input("Insert ID [1-100]: ")
            if not cls.is_valid_id(key_to_verify):
                print("The ID [{}] is not valid, try again".format(key_to_verify))
            else:
                return key_to_verify

    @classmethod
    def read_and_verify_user_name(cls):
        while True:
            value_to_verify = input("Insert Name to 8 characters [lowercase]: ")
            if not cls.is_valid_name(value_to_verify):
                print("The Name [{}] is not valid, try again".format(value_to_verify))
            else:
                return value_to_verify

    @classmethod
    def read_and_verify_one_digit_id(cls):
        while True:
            id_to_verify = input("Please insert user id [1 digit]: ")
            if not cls.is_valid_one_digit_id(id_to_verify):
                print("The digit [{}] is not valid, try again".format(id_to_verify))
            else:
                return id_to_verify

    @classmethod
    def get_match_users_with_id(cls):

        user_id = int(cls.get_user_id_one_digit())
        result = []
        pattern = re.compile('^{}'.format(str(user_id)))
        for user_id in dictionary_global.keys():
            if pattern.match(str(user_id)):
                result.append(dictionary_global.get(user_id))
        return result

    @classmethod
    def get_user_id_one_digit(cls):
        while True:
            try:
                return int(cls.read_and_verify_one_digit_id())
            except ValueError:
                print("Is not valid number, please try again.")
                pass

    @classmethod
    def is_valid_id(cls, user_id):

        return int(user_id) in range(1, 101)

    @classmethod
    def is_valid_name(cls, user_name):
        return re.fullmatch("[a-z0-9]{1,8}", user_name)

    @classmethod
    def is_valid_one_digit_id(cls, id_to_verify):
        return re.fullmatch("[1-9]", str(id_to_verify))

    @classmethod
    def show_users_by_id(cls):
        print("====== User List by ID ======")
        print(cls.get_match_users_with_id())

    @classmethod
    def show_by_group(cls):
        print("====== User List by Group ======")
        for user_id in dictionary_global.keys():
            user_id_to_compare = int(user_id)
            if user_id_to_compare in range(1, 26):
                print("[Group #1] [{}]-> {}".format(user_id, dictionary_global.get(user_id)))
            elif user_id_to_compare in range(26, 51):
                print("[Group #2] [{}]-> {}".format(user_id, dictionary_global.get(user_id)))
            elif user_id_to_compare in range(51, 76):
                print("[Group #3] [{}]-> {}".format(user_id, dictionary_global.get(user_id)))
            else:
                print("[Group #4] [{}]-> {}".format(user_id, dictionary_global.get(user_id)))

    @classmethod
    def run_practice_one(cls):
        print("[USERS] [REGEX] PRACTICE 3")
        cls.fill_dictionary()  # 1,2
        cls.show_by_group()  # 4
        cls.show_users_by_id()  # 3


script = UserManager
script.run_practice_one()
