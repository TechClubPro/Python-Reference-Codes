import datetime

bday = datetime.date(1983,9,17)
today = datetime.date.today()

age = today - bday
print(age)
print(age.days)

"""
Calculating age in more elaborate terms like hrs, mins....etc
"""
bday = datetime.datetime(1983,9,17,10,35,32,100000)
today = datetime.datetime.now()

age = today - bday
print(age)
print(age.total_seconds())