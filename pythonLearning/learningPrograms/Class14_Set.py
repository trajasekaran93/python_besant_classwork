
# set characteristics
# Duplicate value is not allowed
# enclosed with curly braces
# index and slicing concepts cannot performed
# set is heterogenious allow different types of datatypes
# order is not preserved and print in random order
# cannot perform index based operations



s={ }
print(type(s))  # return type is dict

s= { 10,20,30,40,50,60,10,20,"run"}
print(type(s))  # return type is set
print(s)  # remove duplicates and print in random order

# print(s[3])  # index and slicing concepts cannot worked - throws TypeError: 'set' object is not subscriptable

s.add(34)  # it will add anywhere in the list
print(s)

s.pop()  # randomly it will remove value from the list
print(s)

lang= { "java"," python"," sql"}
print(lang)
lang.add("c++")  # add value at any where in the list
print(lang)

lang.update(["perl"," groovy"])  # used to add multiple value
print(lang)

print(len(lang))  # returns the length of the list starts from 1

lang.remove("java")  # remove the given value from the set
print(lang)  # we cannot remove multiple values at a time

col1= { "red"," blue"," green"," yellow"}
col2= { "red"," black"," green"," white"," orange"}

print("union: ", col1 | col2)  # returns value from both set but duplicate removed

print("intersection :" , col1 & col2)  # returns common values from both set

print("difference set 1:" , col1 - col2)  # returns unique value from first set

print("difference set 2:" , col2 - col1)  # returns unique value from second set





