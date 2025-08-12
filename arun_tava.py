# time_list = [
#     "09:00", "10:00", "11:30", "14:00", "14:30", "18:30"]
# print(type(time_list[1]))

# from datetime import datetime,timedelta

# def calculate_time_difference(time_str1, time_str2):
#     FMT = '%H:%M'
#     time1 = datetime.strptime(time_str1, FMT)
#     time2 = datetime.strptime(time_str2, FMT)

    
#     time_difference = time2 - time1
#     return time_difference




# def calculate_working_hour(time_list):
#     start_time=time_list[0]
#     working_hour=timedelta(days=1)
#     for i in range(1,len(time_list)):
#         if i%2!=0:
#             end_time=time_list[i]
#             difference = calculate_time_difference(start_time, end_time)
#             print(start_time,end_time)
#             start_time=end_time
#             working_hour+=difference     
#         else:
#             end_time=time_list[i]
#             start_time=end_time
#     return working_hour
            
# print(calculate_working_hour(time_list)-timedelta(days=1))      


def get_prime_factorial(num):
     factorial=[]
     list_possibel_factorial=[]
     for i in range(2,num):
         if num%i==0:
             factorial.append(i)
     
     for j in range(len(factorial)):
         temp=factorial[j]
         for k in range(j+1,len(factorial)):
             temp*=factorial[k]
             if temp==num:
                 list_possibel_factorial.append(factorial[j:k+1])
                 
             
     return list_possibel_factorial
             
print(get_prime_factorial(12))