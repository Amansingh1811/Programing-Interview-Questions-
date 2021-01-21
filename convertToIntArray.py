def convertToIntArray(strArr: []):
    length = len(strArr)
    for i in range(length):
        num = strArr[i] 
        if(num == '') :
            strArr[i] = 0
        else:
            strArr[i] = int(num)
    return strArr  
