
# Tuple


t=()
x=(10)
y=(10,20,30)
print(type(t))  # tuple
print(type(x))  # int datatupe bcz we pass only one value
print(type(y))  # tuple datatype we pass multiple values inside paranthesis , by using comma


mytuple = ("red","blue","orange")

for i in mytuple:
    print(i)


for i in range(3):  # last index is 2 so (n-1) 3-1
    print(mytuple[i])

# mytuple[2]="green" # we cannot update new values in tuple, its immutable and hrows TypeError: 'tuple' object does not support item assignment

tupleList=list(mytuple)  # converting tuple datatype into list to perform modification
tupleList[2]="green"  # updating the 2 nd index value with new one
print(tupleList)

tupleList.append("yellow")  # adding new value at the end of the list
print(tupleList)

tupleList.extend(["pink","black"]) # adding multiple values at the end of the list
print(tupleList)

mytuple=tuple(tupleList) # converting list to tuple datatype
print(mytuple)

