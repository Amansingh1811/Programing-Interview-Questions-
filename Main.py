import majority_number as m

mystring = input("enter your string")
myArr = mystring.split(",")
m.findMajority(mystring)

myIntArr = m.convertToIntArray(myArr)

print("hello")
# findMajority(arr, n)