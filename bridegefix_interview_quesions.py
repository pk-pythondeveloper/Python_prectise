# # st="12223116"

# # lst=[]
# # count=1
# # for i in range(len(st)):
# #     tp=(int(st[i]),)
# #     if i<len(st)-1:
# #         if st[i]==st[i+1]:
# #             count+=1
# #         else:
# #             temp_count=(count,)
# #             new=tp+temp_count
# #             lst.append(new)
# #             count=1
# #     else:
# #         temp_count=(count,)
# #         new=tp+temp_count
# #         lst.append(new)
        
        
# # print(lst)
# # print(type(lst))
# # print(dict(lst))

# # lst=[(1, 1), (2, 3), (3, 1), (1, 2), (6, 1)]
# # # print(dict(lst))

# # # print({(1,2)})
# # for i in lst:
# #     print(i)


# lst=[1,2,5,3,7]
# def check_smallest(elment11,element2):
#     if elment11<element2:
#         return elment11
#     else:
#         return element2


# def water_content(lst):
#     water_content=0
#     temp=0
    
#     for i in range(0,len(lst)): 
#         for j in range(i+1,len(lst)): 
#             smallest=check_smallest(lst[i],lst[j])
#             temp=(j-i)*smallest
#             if temp>water_content:
#                 water_content=temp
#     return water_content
        
# print(water_content(lst))
 
  
dic = { 
      
       }