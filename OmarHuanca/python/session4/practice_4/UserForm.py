import re

dictionary_global = {}


class UserForm:

    @classmethod
    def read_valid_username(cls):
        while True:
            username_to_verify = input("Insert Username [lowercase(a-z), number (0-9), an underscore]: ")
            if not cls.is_valid_username(username_to_verify):
                print("The Username [{}] is not valid, try again".format(username_to_verify))
            else:
                return username_to_verify

    @classmethod
    def read_valid_password(cls):
        while True:
            password_to_verify = input("Insert Password [lowercase letter (a-zA-Z0-9) and 8-16 characters]: ")
            if not cls.is_valid_password(password_to_verify):
                print("The Password [{}] is not valid, try again".format(password_to_verify))
            else:
                return password_to_verify

    @classmethod
    def read_valid_email(cls):
        while True:
            email_to_verify = input("Insert vail email [anything@domain.com]: ")
            if not cls.is_valid_email(email_to_verify):
                print("The Email [{}] is not valid, try again".format(email_to_verify))
            else:
                return email_to_verify

    @classmethod
    def is_valid_username(cls, username):
        return re.fullmatch("[a-z0-9_]+", username)

    @classmethod
    def is_valid_password(cls, password):
        return re.fullmatch("[a-zA-Z0-9]{8,16}", password)

    @classmethod
    def is_valid_email(cls, email):
        return re.fullmatch("([\w.]+)@([\w.]+)", email)

    @classmethod
    def show_user_information(cls):
        username = cls.read_valid_username()
        password = cls.read_valid_password()
        email = cls.read_valid_email()
        print("====== Valid Information ======")
        print("Username: {}".format(username))
        print("Password: {}".format(password))
        print("E-Mail: {}".format(email))

    @classmethod
    def run_practice_one(cls):
        print("[USERS] [REGEX] PRACTICE 3")
        cls.show_user_information()


script = UserForm
script.run_practice_one()
