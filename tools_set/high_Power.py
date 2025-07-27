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
printIncreasingPower(100)