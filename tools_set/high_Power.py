def printIncreasingPower(x):
    #code here
    i=1
    # Loop to jump in powers of 2
    while(i<=x):
        #code here
        if (i*i<=x):
            print ( i*i, end=' ')
        i+=1
        #code here
#printIncreasingPower(100)

def decrementList(arr):
    #code here
    for i in arr:
        print(int(i-1), end=" ")

arr = [54, 43, 2, 1, 5]
#decrementList(arr)

def isPalindrome(s):
    for i in range (len(s)):
        if (s[i] == s[-(i+1)]):
            p = True
        else:
            p = False
            break
    return p

isPalindrome("abba")