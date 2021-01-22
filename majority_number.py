import convertToIntArray as c

def findMajority(param) -> None:
    arr = param.split(",")
    n = len(arr)
    arr = c.convertToIntArray(arr)
    maxcount = 0 
    index = -1 
    for i in range(n):
        count = 0
        for j in range(n):
            if(arr[i] == arr[j]):
                count += 1
        if (count > maxcount):
            maxcount = count
            index = i
    if (maxcount > n//2): 
        print("Majority number is - ",arr[index])
        print("Majority number count ", maxcount)
    
    else:
        print("no Majority Element")
        


def printmNnumber(strArr: [], n:int) -> int:
    index = n -1
    return  strArr[index]

