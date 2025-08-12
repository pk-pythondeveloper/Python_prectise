student_data=[
  {
    "objid": 1,
    "full_name": "Amit Kumar",
    "contact": "9876543210",
    "age": '23Y 11M',
    "softdelete": False
  },
  {
    "objid": 2,
    "full_name": "Priya Sharma",
    "contact": "9876501234",
    "age": '28Y 1M',
    "softdelete": False
  },
  {
    "objid": 3,
    "full_name": "Rohan Mehta",
    "contact": "9998877665",
    "age": '33Y 9M',
    "softdelete": True
  },
  {
    "objid": 4,
    "full_name": "Sneha Verma",
    "contact": "8887766554",
    "age": '23Y 4M',
    "softdelete": False
  },
  {
    "objid": 5,
    "full_name": "Vikash Yadav",
    "contact": "9090909090",
    "age": '23Y 11M',
    "softdelete": True
  }
]


new_records = [
  {
    "first_name": "Amit",
    "last_name": "Kumar",
    "contact": "9876543210",
    "dob": "2002-05-14",
    "Event": 1
  },
    {
    "first_name": "prince",
    "last_name": "yadav",
    "contact": "98773210",
    "dob": "2002-05-14",
    "Event": 1
  },
  {
    "objid":1,
    "first_name": "Priya",
    "last_name": "Sharma",
    "contact": "9876501234",
    "dob": "2001-09-30",
    "Event": 2
  },
  {
    "objid":2,
    "first_name": "Rohan",
    "last_name": "Mehta",
    "contact": "9998877665",
    "dob": 34,
    "Event": 3
  }
]

# n=student_data[0]
# n["softdelete"]=True
# print(n)
from datetime import datetime

def calculate_age(birthdate_str):


    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    except ValueError:
        return None, None 

    current_date = datetime.now()

    years = current_date.year - birthdate.year
    if (current_date.month < birthdate.month) or \
       (current_date.month == birthdate.month and current_date.day < birthdate.day):
        years -= 1

    months = (current_date.month - birthdate.month) % 12
    if current_date.month < birthdate.month:
        months = 12 + months
    Y=f"{years}Y "
    M=f"{months}M"
    
    return Y,M


def maintain_student_record(student_data,new_records):
  
    # breakpoint()
    last_student=student_data[-1]
    last_stu_id=last_student["objid"]
    
    for i in new_records:
        if i["Event"]==1:
            iteam=i.popitem()
            i.update({"objid":last_stu_id+1})
            i.update({"full_name":i["first_name"]+" "+i["last_name"]})
            i.pop("first_name")
            i.pop("last_name")
            
            # breakpoint()
            birth_date=calculate_age(i["dob"])
            age=birth_date[0]+birth_date[1]
            i["age"]=age
            i.pop("dob")
            i["softdelete"]=False
            student_data.append(i)
            last_stu_id+=1
            
        elif i["Event"]==2 or i["Event"]==3:
            for j in student_data:
                if i["objid"]==j["objid"]:
                    if i["Event"]==2:
                        j["full_name"]=i["first_name"]+" "+i["last_name"]
                        j["contact"]=i["contact"]
                        birth_date=calculate_age(i["dob"])
                        age=birth_date[0]+birth_date[1]
                        i["age"]=age
                        
                      
                        i.pop("dob")
                        j["softdelete"]=False
                
                    elif(i["Event"]==3):
                        j["softdelete"]=True
    print(student_data)
    for data in student_data:
      print(data)
      
    
            
            
    
maintain_student_record(student_data,new_records)