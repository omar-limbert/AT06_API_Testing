"""
Module to Calculate age in minutes, hours and days
"""


def get_age_in_days(age):
    return age * 365


def get_age_in_hours(age):
    return get_age_in_days(age) * 24


def get_age_in_minutes(age):
    return get_age_in_hours(age) * 60
