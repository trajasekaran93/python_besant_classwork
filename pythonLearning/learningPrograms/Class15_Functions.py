


# functions


def welcome():  # methods without parameters
    print("welcome to python class")

welcome()  # calling the method name


def func(name):  # functions with parameter
    print("welcome to python class : ",name)

func("raju")


def fun(name,age,grade):
    print("name is :",name)
    print("age is :", age)
    print("grade is :",grade)

fun("raju"," 23"," A")
fun(12,13,14)
fun(age=23,name='raju',grade='A')
fun(age=23,name="raju",grade="A")
fun("sekar",age=12,grade="B")     # name is positional argument, age and grade is keyword argument
                                        # python allow to keyword arg followed by positional arg
# fun(age=24,"Geetha",grade="AA")       # throws error - python doesn't allow positional arg followed by keyword arg
# fun("remo",23,age=43) # throws error -  TypeError: fun() got multiple values for argument 'age'


# Default value
def met(name,age=12,grade=9):  # age and grade have default value
    print(name)
    print(age)
    print(grade)

met("halik")  # remaining parameter take from default value
met("remo",13)  # remaining last parameter take from the default
met("sara",34,"A")  # if we pass all parameter then python don't refer default value


def val(x=1):
    a= x + 1
    b= x * 3
    c= a **2
    print("a :",a )
    print("b :",b )
    print("c :",c )


val()  # take default vaule x=1
val(2)  # take the 2 as x value


def new(*n):
    for i in n:
        print("value is:",i )


new(1)
new(2,3,4 )
new(22,33,434,232)


def sum(*n,name):
        result=0
        for x in n:
            result=result+x
            print("result by: ",name,": ",result)

sum(name="raju")  # doesn't print because of parameter missing
sum(12,name="raju")
sum(66,34.56,name="raju")
# sum(name="been",12,23,) # throws error - Positional argument after keyword argument not support


# def sum(name,*y):
#         # print(type(sum()))
#         result=0
#         for x in y:
#             result=result+y
#             print("result by: ",name,": ",result)
#
# sum("raju",12) # throws error - TypeError: unsupported operand type(s) for +: 'int' and 'tuple'


# ARBITARY ARGUMENTS
def disp(**x):
    print(type(x))
    for k,v in x.items():  # .items() method will iterate by one key value pair , returs list of tuple

        print(k," ----",v )

disp(name="raju",sal=1211234)
disp(bus="rathimeena",ticket=560,seat="semi sleeper",traveltime="7 hrs")


def ret1(a,b):
    c=a+b
    return  c

print(ret1(11,42)) # print statement include with method namess s
