#Create a function that calculates the age of user on passing DOB.
# [Hint: You can get current date from datetime library, use AI tool for detail].
# Note: You need to raise Exception if DOB is in invalid format, if DOB is in future.
# Return value of age has to be integer number.
from datetime import datetime


def calculate_of_age(user_dob):
    current_date = datetime.now()
    user_dob_date = datetime.strptime(user_dob, "%Y-%m-%d")

    if user_dob_date > current_date:
        raise ValueError("DOB In future")

    user_age = current_date - user_dob_date
    return user_age.days // 365



result = calculate_of_age('2004-12-12')
print(result)