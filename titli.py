'''
Enter the row size for the pattern: 5
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 

'''
for i in range(1,11):
    for j in range(1,11):
        if i<6:
            if j<i+1 or j>10-i:
                print("*",end="")
            else:
                print(" ",end="")
                
        else:
            if j<12-i or j>=i:
                 print("*",end="")
            else:
                print(" ",end="")
    print()