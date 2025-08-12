'''
* 
* * 
*   * 
*     * 
* * * * * 

''' 

for i in range(1,6):
    for j in range(1,6):
        if i==5:
            print("*",end="")
        elif j==1:
            print("*",end="")
        elif j>1 and j<5:
            if j==i:
                print("*",end="")
            else:
                print(" ",end="")
       
    print()
    


