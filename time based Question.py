import time
import datetime

score=0

t1 = datetime.datetime.now()
ans = input("Capital of Odisha?")


if ans=="a":
    print("Correct Ans" )
    score = score + 1
else:
    print("Wrong ans")
    score = score -1
t2 = datetime.datetime.now()

delay = t2- t1

if delay.total_seconds() > 5:
    print("Sorry You took more time. So Bye")
    print("Time taken" + str(delay.total_seconds()))
else:
    print("You are quick")