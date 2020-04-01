import datetime
import time

num1 =6
num2 =4
num3 =7
num4=1
num5=5

score =0

print("Memorize")
print(num1)
time.sleep(1)
print(num2)
time.sleep(1)
print(num3)
time.sleep(1)
print(num4)
time.sleep(1)
print(num5)
time.sleep(1)

for x in range(10):
    print("*"*x)

t1 = datetime.datetime.now()

for x in range(1,6,1):
    ans = int(input("Enter the Number in sequence"))
    
    if x==1 and ans == 6:
        score = score+1
    elif x==2 and ans == 4:
        score = score+1
    elif x==3 and ans == 7:
        score = score+1
    elif x==4 and ans == 1:
        score = score+1
    elif x==4 and ans == 0:
        score = score+1
    else:
        score =score -1
t2 = datetime.datetime.now()

delay = t2 -t1
print("Your score is "+ str(score))
print("Time you took :" + str(delay.total_seconds()))

