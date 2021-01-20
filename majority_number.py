def findMajority(myString):
    arr = myString.split(",")
    n = len(arr)
    arr = convertToIntArray(arr)
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
        
        

def convertToIntArray(strArr: []):
    for i in range(len(strArr)):
        strArr[i] = int(strArr[i])    
    return strArr  

