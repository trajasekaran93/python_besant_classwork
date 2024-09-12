
# Replace value using %i

a,b,c=10,20,30

print("a value is %i" %a)
print("b value is %i and c value is %i" %(b,c))

# Replace value using {}

name = "RAJU"
sal = 300000
company = "VIRTUSA"

print("hai {0} your salary is {1}".format(name,sal))
print("Hai {} your company name is {}".format(name,company))
print("your company name is {c} and your salary is {b} and your name is {a}".format(a=name,b=sal,c=company))


# Swaping the value using temp

a=5
b=7
print("a value is {} and b vaue is {}".format(a,b))

temp=a
a=b
b=temp
print("a value is {} and b vaue is {}".format(a,b))