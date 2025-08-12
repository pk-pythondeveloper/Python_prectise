student_data=[
  {
    "objid": "S001",
    "name": "Amit Kumar",
    "contact": "9876543210",
    "dob": "2002-05-14",
    "softdelete": False
  },
  {
    "objid": "S002",
    "name": "Priya Sharma",
    "contact": "9876501234",
    "dob": "2001-09-30",
    "softdelete": False
  },
  {
    "objid": "S003",
    "name": "Rohan Mehta",
    "contact": "9998877665",
    "dob": "2003-02-25",
    "softdelete": True
  },
  {
    "objid": "S004",
    "name": "Sneha Verma",
    "contact": "8887766554",
    "dob": "2000-12-10",
    "softdelete": False
  },
  {
    "objid": "S005",
    "name": "Vikash Yadav",
    "contact": "9090909090",
    "dob": "2002-07-22",
    "softdelete": True
  }
]


new_records = [
  {
    "name": "Amit Kumar",
    "contact": "9876543210",
    "dob": "2002-05-14",
    "softdelete": False,
    "Event": 1
  },
  {
    "name": "Priya Sharma",
    "contact": "9876501234",
    "dob": "2001-09-30",
    "softdelete": False
  },
  {
    "objid": "S003",
    "name": "Rohan Mehta",
    "contact": "9998877665",
    "dob": "2003-02-25",
    "softdelete": True
  }
]

print("enter 1 for add ,two for update, 3 for for delete")

value=int(input("enter operation number:-"))

def check_obj_id(stu_obj_id,student_data):
  # breakpoint()
  temp=0
  for j in student_data:
    if j["objid"]==stu_obj_id:
      temp+=1
  if temp>0:
    return True
  else:
    False
      
def maintain_student_record(student_data,value):
  # breakpoint()
  if value==3 or value==2: 
    stu_obj_id=input("plese enter your obj id:-")
    if stu_obj_id:
      for i in student_data:
          if i["objid"]==stu_obj_id:
            if value==3:
              i["softdelete"]=True
              print("given data deleted succesfully  ")
              break
            elif value==2:
              name=input("enter new name:-")
              contact=input("enter your contect number:-")
              dob=input("enter data of birth:-")
              i["softdelete"]=False
              if name:
                i["name"]=name
              if contact:
                i["contact"]=contact
              if dob:
                i['dob']=dob
              print(i)
              print("data updated succesfully")
  elif(value==1): 
    objid=input("enter obj id:-")
    
    if not check_obj_id(objid,student_data):
      name=input("enter new name:-")
      contact=input("enter your contect number:-")
      dob=input("enter data of birth:-")
      student_data.append({
            "objid": objid,
            "name": name,
            "contact": contact,
            "dob": dob,
            "softdelete": False
                    }) 
      print("data added succesfully")  
      
    else:
      print("plese use diffrent id ") 
      
  return student_data
        
        
maintain_student_record(student_data,value)