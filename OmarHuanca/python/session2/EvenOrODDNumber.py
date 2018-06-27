class EvenOrODDNumber:

    @classmethod
    def is_odd_or_even(cls, number):
        return 'even' if number % 2 == 0 else 'odd'

    @classmethod
    def check_even_or_odd_numbers_on_range(cls, min, max):
        result = []
        for numbers in range(min, max + 1):
            result.append("{} : is {}".format(numbers, cls.is_odd_or_even(numbers)))
        return result
