def findMajority():
    arr = [1, 1 , 5, 1, 3, 5, 1]
    n = len(arr)
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
        
        

