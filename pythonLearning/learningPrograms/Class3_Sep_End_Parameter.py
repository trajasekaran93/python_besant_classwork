import sys

# Seperator parameter in python

print ('raju','rock','sekar')
print ('raju','rock','sekar', sep='')  # print without space
print ('raju','rock','sekar', sep=',')  # print with comma separator
print ('raju','rock','sekar', sep=': ')  # print with colan separator

x= "raj","peter","sathis"
print (x)
print(x, sep=':')  # it won't separator with colon

a,b,c = 10,11,12
print(a,b,c)
print(a,b,c, sep=('&'))

# end parameter in python

print("raju is")
print ("good boy")

print("raju is", end='')  # now end parameter will append the next print statement in a same line
print ("good boy")

print("raju is", end='@')  # now it will append @ synmbol with the next print statement
print ("good boy")

print("raju is", end=' very ')  # now it will append @ synmbol with the next print statement
print ("good boy")

print(1,2,3, sep=',', end='...')
print(9,10, sep=',')

# file parameter ued to write input from python into text file

# print(value,...,sep='', end='/n', file=sys.stdout, flush=False) ---> DEFAULT PRINT STATEMENT INBUILT PARAMETERS


