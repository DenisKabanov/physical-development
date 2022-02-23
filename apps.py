import datetime


def determine_the_passport_age(dob, doi):
    age = doi - dob
    return age
