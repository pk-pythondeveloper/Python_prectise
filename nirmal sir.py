'''
*
**
***
****
*****


'''




# for i in range(1,6):
#     if i<i+1:
#         print("*",end="")



# main_dict={}
# import  datetime,time
# from time import gmtime, strftime
# def rotaltiosonal_program(sleep_time):
#     now=strftime("%Y-%m-%d %H:%M:%S", gmtime())
#     sleep_in_mnutes=sleep_time*60
#     time.sleep(sleep_in_mnutes)
    
#     print("Wait until 2 seconds.",now)
#     return rotaltiosonal_program(1.5)

# rotaltiosonal_program(1.5)
 
 
   
dic = {'a':5,  'b' : 50}
input=input('enter yor keys')

count=0
for i in dic.keys():
    if i!=input:
        count+=1
if count<1:
    raise ValueError('keys not found')
else:
    raise V