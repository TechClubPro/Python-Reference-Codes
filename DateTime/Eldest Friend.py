import time
import datetime

F1 = datetime.date(2010,3,17)
F2 = datetime.date(2010,12,23)
F3 = datetime.date(2009,2,5)
F4 = datetime.date(2009,8,17)

today = datetime.date.today()

age_F1 = (today - F1).total_seconds()
age_F2 = (today - F2).total_seconds()
age_F3 = (today - F3).total_seconds()
age_F4 = (today - F4).total_seconds()

print("Ages in Seconds:")
print(age_F1)
print(age_F2)
print(age_F3)
print(age_F4)

if age_F1>age_F2:
    list1 = age_F2
    list2 = age_F1
else:
    list1= age_F1
    list2 = age_F2
    
if list2>age_F3:
    list3=list2
    list2=age_F3
else:
    list3=age_F3

if list3>age_F4:
    list4=list3
    list3 = age_F4
else:
    list4=age_F4
    
print("Age in Ascending order ")
time.sleep(1)
print(list1)
time.sleep(1)
print(list2)
time.sleep(1)
print(list3)
time.sleep(1)
print(list4)
time.sleep(1)

#if age_F1>age_F2 and age_F1>age_F3 and age_F1>age_F4:
#    print("Age F1 biggest")
#    list1 = age_F1
#elif age_F2>age_F1 and age_F2>age_F3 and age_F2>age_F4:
#    print("Age F2 biggest")
#    list1 = age_F2
#elif age_F3>age_F1 and age_F3>age_F2 and age_F3>age_F4:
#    print("Age F3 biggest")
#    list1 = age_F3
#else:
#    print("F4")
#    list1 = age_F4
#    
#if age_F1<age_F2 and age_F1<age_F3 and age_F1<age_F4:
#    print("Age F1 smallest")
#    list4 = age_F1
#elif age_F2<age_F1 and age_F2<age_F3 and age_F2<age_F4:
#    print("Age F2 samllest")
#    list4 = age_F2
#elif age_F3<age_F1 and age_F3<age_F2 and age_F3<age_F4:
#    print("Age F3 smallest")
#    list4 = age_F3
#else:
#    print("F4")
#    list4 = age_F4   
#    
##print(list1)
##print(list4)
#
#if list1 ==age_F1:
    