'''
Enter the row size for the pattern: 5
*      * 
  *   *   
    *     
  *   *   
*       * 

=== Code Execution Successful ===

'''


for i in range(1,6):
    for j in range(1,6):
        if i<4:
            if j==i or j==6-i:
                print("*",end="")
            else:
                print(" ",end="")
            
        else:
            if j==6-i or j==i:
                print("*",end="")
            else:
                print(" ",end="")
    print()