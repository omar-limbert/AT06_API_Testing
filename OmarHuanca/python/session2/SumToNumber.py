class SumToNumber:

    @classmethod
    def sum_to_number(cls, number):
        sum = 0
        for i in range(1, number + 1):
            if i > 35:
                return sum
            sum += i
        return sum
