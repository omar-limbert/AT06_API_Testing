class FillListFromUser:

    @classmethod
    def fill_list_from_input(cls):

        length_of_list = cls.read_length_of_list()
        result_list = []
        for i in range(1, int(length_of_list) + 1):
            result_list.append(input("Enter element #{}: ".format(i)))
        return result_list

    @classmethod
    def read_length_of_list(cls):
        while True:
            try:
                return int(input('How many elements you need on list?: '))
            except ValueError:
                print("Is not valid Length please try again.")
                pass


script = FillListFromUser
print("Input List: {}".format(script.fill_list_from_input()))
