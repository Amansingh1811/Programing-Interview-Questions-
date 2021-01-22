import majority_number as m
import array_length as a
import convertToIntArray as c


promptStr = "Please enter your value: "
userstring = input(promptStr)

arrLen: int  = a.lengthofarray(userstring)
print("your array length is ", arrLen)

m.findMajority(userstring)

arrtype = userstring.split(",")
intArr = c.convertToIntArray(arrtype)
print("Int Array: ", intArr);

nthNumber = int(input("enter your nth number: "))
nn = m.printmNnumber(intArr, nthNumber)
print("your nth number is ", nn)
