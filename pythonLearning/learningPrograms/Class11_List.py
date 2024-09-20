from encodings.punycode import insertion_sort

# LIST

fruits = ["apple","orange","banana","cherry","fig","strawberry","mango"]

print(fruits)  # print entire list values
print(len(fruits)) # print length of the list , starts from 1
print(fruits[2]) # print the 2nd index
print(fruits[-1]) # print last index
print(fruits[-3]) # print third value from the reverse

print(fruits[2:5])  # slicing function, print from start indx 2 to end indx 4 (5-1)
print(fruits[1:])  # print from index 1 to last index
print(fruits[5:1]) # print [] , starting index is greater than ending index
print(fruits[-4:-1]) # print from -4 index to -2 index (n-1)
print(fruits[-2:-4]) # print [] , starting index is greater than ending index

print(fruits)
fruits[2]="chicken" # replace the 2nd index value with new value
print((fruits))

for i in fruits:  # iterating using for each loop
    print("fruits present in the list : ",i)

if('orange') in fruits: # using if condition to check the value is present in the list or not
    print("present")
else:
    print("orange is not present")

fruits.append("mutton") # add the new value at the end of the list
print(fruits)
# fruits.append("duck","beef")  # can't allow to add multiple values
# fruits.append(["grapes","plums"])
print(fruits)
print("----")
print(fruits[-6:-1])

fruits.extend(["butter fruit","jack fruit"])  # add multiple values at the end of the list
print(fruits)

fruits.extend("melon")  # it will take each word as single value
print(fruits)
print(fruits[13])

fruits.sort(reverse=True)  # print in reverese alphabetical order
print(fruits)

fruits.sort(reverse=False)  # print in alphabetical order
print(fruits)

fruits.insert(2,"turkey") # newly added the value to the given index, existing value is move one step to the right side
print(fruits)

# fruits.remove("appLe")  # cann't remove multiple values throws - ValueError: list.remove(x): x not in lis
fruits.remove("apple")
print(fruits)

fruits.pop() # remove the last index value from the list
print(fruits)
fruits.append("squid")
print(fruits)
fruits.pop()
print(fruits)

newfruits=fruits.copy() # copy the values from one list to new list
print("new copied fruits list : ",newfruits)

newfruits.append("cherry")
print(newfruits)
print(newfruits.count("cherry")) # ans 2 - return the count of cherry in a list

print(newfruits.index("fig"))  # return the index of the value in a list

newfruits.clear()
print(newfruits)  # clear the values in a list , empty list

# del newfruits
# print(newfruits) # delete the list - NameError: name 'newfruits' is not defined.

# adding two list
list1 = [1,2,3,4,5]
list2 = ["hai","how","are","you"]
res=list2+list1
res2=list1+list2
print(res)  # concat the two lists
print(res2)


#list package

num=[1,2,3,4,5,6,7]
a=num[0]
b=num[1]
c=num[3]  # need to check
a,b,c,d,*others,last=num  # last will take the last index value from the list
print(a)
print(b)
print(c,d)
print(others) # print the remaining values 
print(last)

