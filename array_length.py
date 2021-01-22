import convertToIntArray as c
def lengthofarray(userstring:str) -> int :
    arr = userstring.split(",")
    arr = c.convertToIntArray(arr)
    n = len(arr)
    return n
    