from calendar import day_name

# we are going to use conditional operators
# using Relational operators and Logical Operators

# age=int(input("enter your age : "))
#
# if(age>18):
#     print("Eligible to vote")
# else:
#     print("not eligible to vote")
#
# totmarks = float(input("enter your marks :"))
#
# if(totmarks>=450):
#     print("grade A")
# elif(totmarks>=400):
#     print("Grade B")
# elif(totmarks>=350):
#     print("Grade C")
# else:
#     print("poor mark ")

# totmarks = float(input("enter your marks :"))
#
# if (totmarks >450 and totmarks<=500):
#     print("grade A")
# elif (totmarks >=401 and totmarks<=450):
#     print("Grade B")
# elif (totmarks >=351 and totmarks<=400):
#     print("Grade C")
# elif (totmarks <=350):
#     print("fail mark")
# else:
#     print("invalid mark ")

# enter_Day = input("enter today's name : ")
#
# if(enter_Day=='saturday' or enter_Day=='sunday'):
#     print("your ticket amount is 100 Rs")
# elif(enter_Day!='saturday' or enter_Day!='sunday'):
#     print("your ticket amount is 80 Rs")



consumed_units = float(input("enter the consumed units : "))

if(consumed_units>0 and consumed_units<=100):
    fare =consumed_units*2
    print("your bill amount for" ,consumed_units, "unit is : ",fare)
elif(consumed_units>100 and consumed_units<=200):
    fare =consumed_units*3
    print("your bill amount for" ,consumed_units, "unit is : ",fare)
elif(consumed_units>200 and consumed_units<=300):
    fare =consumed_units*4
    print("your bill amount for" ,consumed_units, "unit is : ",fare)
elif(consumed_units>300 and consumed_units<=500):
    fare =consumed_units*6
    print("your bill amount for" ,consumed_units, "unit is : ",fare)
elif(consumed_units>500 and consumed_units<=700):
    fare = consumed_units * 10
    print("your bill amount for", consumed_units, "unit is : ", fare)
else:
    print("invalid unit entered")