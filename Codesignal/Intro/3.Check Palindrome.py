def checkPalindrome(inputString):
    mid=len(inputString)
    for i in range(0,mid):
        Original = inputString[i]
        Reverse = inputString[len(inputString) - 1 - i]
        if Original != Reverse: 
            return False
    
    return True
