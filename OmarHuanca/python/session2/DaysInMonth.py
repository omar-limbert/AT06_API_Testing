class DaysInMonth:

    @classmethod
    def get_days_in_month(cls, month_to_verify):
        month_dictionary = {
            "january": 31,
            "february": 28,
            "march": 31,
            "april": 30,
            "may": 31,
            "june": 30,
            "july": 31,
            "august": 31,
            "september": 30,
            "october": 31,
            "november": 30,
            "december": 31
        }

        if month_to_verify.lower() in month_dictionary.keys():
            return month_dictionary[month_to_verify.lower()]
        else:
            return "Month not found."
