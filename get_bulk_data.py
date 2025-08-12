student_data=[
  {
    "objid": 1,
    "name": "Amit Kumar",
    "contact": "9876543210",
    "dob": "2002-05-14",
    "softdelete": False
  },
  {
    "objid": 2,
    "name": "Priya Sharma",
    "contact": "9876501234",
    "dob": "2001-09-30",
    "softdelete": False
  },
  {
    "objid": 3,
    "name": "Rohan Mehta",
    "contact": "9998877665",
    "dob": "2003-02-25",
    "softdelete": True
  },
  {
    "objid": 4,
    "name": "Sneha Verma",
    "contact": "8887766554",
    "dob": "2000-12-10",
    "softdelete": False
  },
  {
    "objid": 5,
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
    "Event": 1
  },
    {
    "name": "ppppppp",
    "contact": "987789578543210",
    "dob": "2002-05-14",
    "Event": 1
  },
  {
    "objid":1,
    "name": "Priya Sharma",
    "contact": "9876501234",
    "dob": "2001-09-30",
    "Event": 2
  },
  {
    "objid":2,
    "name": "Rohan Mehta",
    "contact": "9998877665",
    "dob": "2003-02-25",
    "Event": 3
  }
]

# s=student_data[-1]
# print(s["objid"])



def maintain_student_record(student_data,new_records):
    # breakpoint()
    last_student=student_data[-1]
    last_stu_id=last_student["objid"]
    
    for i in new_records:
        if i["Event"]==1:
            iteam=i.popitem()
            i.update({"objid":last_stu_id+1})
            i.update({"":last_stu_id+1})
            student_data.append(i)
            last_stu_id+=1
            
        elif i["Event"]==2 or i["Event"]==3:
            for j in student_data:
                if i["objid"]==j["objid"]:
                    if i["Event"]==2:
                        j["name"]=i["name"]
                        j["contact"]=i["contact"]
                        j["dob"]=i["dob"]
                        j["softdelete"]=False
                    elif(i["Event"]==3):
                        j["softdelete"]=True
    print(student_data)
    print(len(student_data))
            
            
    
maintain_student_record(student_data,new_records)