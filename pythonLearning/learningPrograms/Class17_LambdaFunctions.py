from mailcap import subst

# LAMBDA FUNCTIONS

# ANONYMOUS FUNCTION / NAMELESS FUNCTION
# ITS FOR ONE TIME USE
# CAN PASS ANY NO OF ARGS, BUT IT WILL RETURN ONLY ONE EXPRESSION
# STORING THE PYTHON DATASTRUCTURE (LIST,DICTONARY)

n=lambda a,b:a+b
# print(n(12,21))  # value 12 and 21 will pass to a and b paramter

# n1=int(input("enter a value :"))
# n2=int(input("enter b value :"))
# print(n(n1,n2))  # getting input from user and pass it to lambda func


add=lambda x:x+100
print(add(33))

print((lambda a,b,c:a*b*c)(2,2,3))

ref = lambda a,b,c : a*b*c
print(ref(3,4,5))

add = lambda *n:sum(n)  # *n - we can give n no of args, sum() inbuilt in python for addition operation
print(add(44,32,32,23,3,1,3,5,))

higher=lambda x,fun : x+fun(x)
print(higher(20,lambda x:x*x))

res = lambda x:((x%2==1) and 'odd' or 'even')
print(res(121221))

substring = lambda String: String in "how is python"
print(substring("pythons"))

