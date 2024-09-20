


import random as r

codeword =['hill' ,'ice' ,'mask']
inp=input("enter code word :").lower()

if inp in codeword:
        print("code word is correct")
else:
        print("invalid code word")



a= r.randint(2,10) # randomly print from starting value 2 to ending 10
b= r.randint(2121,10112) # randomly print from starting value to ending value
print(a)
print(b)
c=r.randrange(1,5) # randomly print from starting value from 1 to ending value 4
print(c)
print(c)
d=r.choice(codeword) # randomly choose the value from the list
print(d)