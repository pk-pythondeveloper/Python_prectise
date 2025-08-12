nums = [1, 2,3, 5, 6]
def find_missingnumber(nums):
    actual_sum=sum(nums)
    excepted_sum=0
    for i in range(1,nums[-1]+1):
        excepted_sum+=i
        
        
    return excepted_sum-actual_sum
        
print(find_missingnumber(nums))