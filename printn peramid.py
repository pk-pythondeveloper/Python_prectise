'''
       *
      ***
     *****
      ***
       *
'''
temp=1
for i in range(1,6): 
    for j in range(1,6):
        if (i<=3):
            if j>3-i and j<3+i:
                print("*",end="")
            else:
                print(" ",end="")
        if(i>3):
            if j>temp and j<6-temp:
                print("*",end="")
            else:
                print(" ",end="")
            
    if (i>3):
        temp+=1    
    print()
                
       