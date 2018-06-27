class PrimeNumber:

    @classmethod
    def is_prime(cls, number):

        if number == 0:
            return False
        elif number == 1:
            return True

        for i in range(2, int(abs(number) ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    @classmethod
    def check_prime_numbers_on_range(cls, min, max):
        result = []
        for numbers in range(min, max + 1):
            result.append("{} : is prime? {} ".format(numbers, cls.is_prime(numbers)))
        return result
