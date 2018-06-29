"""
Module to print 4 different messages :
You are a child, when the age is lower than 12
Your are teenager, when the age is between 13 and 17
You are young, when the age is between 18 and 29
You are adult, when the age is greater than 30
"""


def validate_age(age_to_validate):
    if age_to_validate in range(0, 13):
        return "Child"
    elif age_to_validate in range(13, 18):
        return "Teenager"
    elif age_to_validate in range(18, 30):
        return "Young"
    else:
        return "Adult"
