def  tri_recusion(k):
    if (k>0):
        # print(k,"before")
        result=k+tri_recusion(k-1)
        print(result,"betweeen")
        print(k,"after")
        print("result",result)
        # print("idhar aaya")
    else:
        result=0
    return result

print(tri_recusion(6))