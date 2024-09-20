

# Dictonaries - it is a key:value pair

dic={}
print(type(dic))  # dict

books = {"j.k rowling":"Philosopher's stone","roald dahl":"matilda","o.hendry":"the last leaf"}
print(books)

print(books["j.k rowling"]) # return the corresponding value of this key

books["enid bylton"]="the secret seven"  # add at the end of the dictonary
print(books)

num={"a":{"1","one"},"b":{"2","two"},"c":{3,"three"}}  # assigning two values for single key
print(num)
print(num["c"]) # returns values of the given key


students={"mn01":{"raju",1234},"mn02":{"rock",2345},"mn03":{"sekar",3456},"mn04":{"bhai",4567}}
print(students)
students["mn05"]="sathis","5678"
students["mn06"]="aravind","6789"
students["mn07"]={"kalai","7890"}
print(students)
# print(students["mn06"])
# print(students["mn07"])

print(students.keys())  # print the keys alone
print(students.values()) # print values alone

for i in students:
    # print(students)
    print(i)  # return the keys from the dictonary
    print(students[i]) # returns the values of the dictonary

# duplicate values allowed

names={"101":"ganga","102":"harini","103":"devi","104":"harini"}
print(names)  # duplicate values are allowed

# won't allow duplicate key, recent value will append on the existing value
names={"101":"ganga","102":"harini","103":"devi","101":"yamini"}
print(names)  # duplicate key are not allowed, it will take the last updated value- ganga was replaced with yamini

name2=names.copy()
print("new dict name : ",name2)

print(name2.pop("101")) # remove the 101 key and corresponding value
print(name2) #

# Merge Dictonary

empname ={"arun":"int tester","angu":"functional tester","princy":"automation tester"}
empdet = {"mobile":"239874","network":"airtel","recharge":"230"}

overall = {"empname" : empname, "empdetails":empdet }
print(overall)
# all ={empname:empdet}  # throws error - TypeError: unhashable type: 'dict'
# print(all)



