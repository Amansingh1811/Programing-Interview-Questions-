import majority_number as m
import convertToIntArray as c

mystring = input("enter your comma seperated string(list): ")
myArr = mystring.split(",")
z = m.findMajority(mystring)

intArr = c.convertToIntArray(myArr)
print("Int Array: ", z);

nthNumber = int(input("enter your nth number: "))
nn = m.printmNnumber(myArr, nthNumber)
print("your nth number is ", nn)