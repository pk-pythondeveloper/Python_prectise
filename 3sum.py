
#first way to soleve
# class Solution():
    
#     def threeSum(self, nums):
#         new_list=[]
#         for i in range(len(nums)):
#             temp=1
#             temp_list=[nums[i]]
#             for j in range(i+1,len(nums)):
#                 if i !=j:
#                     temp_list.append(nums[j])
#                 if len(temp_list)==3 and sum(temp_list)==0:
#                     new_list.append(temp_list)
#                     temp_list=[nums[i]]
#         print(new_list)
        
# nums = [-1,0,1,2,-1,-4]
# obj=Solution()
# obj.threeSum(nums)

#solve using one loop

class Solution():
    
    def threeSum(self, nums):
        new_list=[]
        n=len(nums)
        pre,next=0,n-1
        temp=[]
        if not len(nums)<3:
            print("aaya")
            for i in range(1,n):
                
                temp=[nums[pre],nums[i],nums[next]]
                print(temp)
                if sum(temp)==0 and next!=i:
                    new_list.append(temp)
                    pre+=1
                    next-=1
                    
                pre+=1
                next-=1
                
        print(new_list)
          
        
        
nums = [-1,0,1,2,-1,-4]
obj=Solution()
obj.threeSum(nums)

