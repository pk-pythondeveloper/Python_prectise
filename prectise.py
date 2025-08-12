hospital_a=[
  { "first_name": "Rahul", "last_name": "Verma", "admit_date": "2025-06-01", "disease": "Fever" },
  { "first_name": "Priya", "last_name": "Mehta", "admit_date": "2025-06-02", "disease": "Malaria" },
  { "first_name": "Aman", "last_name": "Shah", "admit_date": "2025-06-03", "disease": "Covid-19" },
  { "first_name": "Sneha", "last_name": "Rathi", "admit_date": "2025-06-04", "disease": "Dengue" },
  { "first_name": "Rohit", "last_name": "Singh", "admit_date": "2025-06-05", "disease": "Asthma" },
  { "first_name": "Kavita", "last_name": "Iyer", "admit_date": "2025-06-06", "disease": "Fracture" },
  { "first_name": "Nikhil", "last_name": "Sinha", "admit_date": "2025-06-07", "disease": "Diabetes" },
  { "first_name": "Alok", "last_name": "Gupta", "admit_date": "2025-06-11", "disease": "Typhoid" },
  { "first_name": "Simran", "last_name": "Kaur", "admit_date": "2025-06-09", "disease": "Migraine1" },
  { "first_name": "Deepak", "last_name": "Bhatt", "admit_date": "2025-06-10", "disease": "Jaundice" },
  { "first_name": "Priya", "last_name": "Kumari", "admit_date": "2025-06-02", "disease": "Malaria" },
  { "first_name": "Simran", "last_name": "Kaur", "admit_date": "2025-06-09", "disease": "Migraine" }
]

hospital_b=[
  { "first_name": "Priya", "last_name": "Mehta", "admit_date": "2025-06-02", "disease": "Malaria" },
  { "first_name": "Aman", "last_name": "Shah", "admit_date": "2025-06-03", "disease": "Covid-19" },
  { "first_name": "Alok Kumar", "last_name": "Gupta", "admit_date": "2025-06-08", "disease": "Typhoid" },
  { "first_name": "Deepak", "last_name": "Bhatt", "admit_date": "2025-06-10", "disease": "Jaundice" },
  { "first_name": "Simran", "last_name": "Kaur", "admit_date": "2025-06-09", "disease": "Migraine" },
  { "first_name": "Meena", "last_name": "Tripathi", "admit_date": "2025-06-11", "disease": "Fracture" },
  { "first_name": "Tarun", "last_name": "Agarwal", "admit_date": "2025-06-12", "disease": "Typhoid" },
  { "first_name": "Neha", "last_name": "Yadav", "admit_date": "2025-06-13", "disease": "Asthma" },
  { "first_name": "Ramesh", "last_name": "Joshi", "admit_date": "2025-06-14", "disease": "Covid-19" },
  { "first_name": "Anjali", "last_name": "Rao", "admit_date": "2025-06-15", "disease": "Fever" },
  { "first_name": "Alok", "last_name": "Gupta", "admit_date": "2025-06-08", "disease": "Typhoid" },
  { "first_name": "Simran", "last_name": "Kaur", "admit_date": "2025-06-08", "disease": "Migraine" }
]


def compare_with_final_list(data,k):
    temp=0
    if data["first_name"]==k["first_name"]:
        temp+=1
    if data["last_name"]==k["last_name"]:
        temp+=1
    if data["admit_date"]==k["admit_date"]:
        temp+=1
    if data["disease"]==k["disease"]:
        temp+=1
    if temp==4:
        return True
    else:
        return False
    

def check_in_final(data,final_list):
    temp1=0
    for k in final_list:
        if compare_with_final_list(data,k):
            temp1+=1
    if temp1<1:
        return True
    else:
        False

    
def get_final_record(hopital_a,hospital_b):
    final_list=[]
    for i in hopital_a:
        if len(final_list)<1:
            final_list.append(i)
        else:
            if check_in_final(i,final_list):
                final_list.append(i)
    for j in hospital_b:
        if len(final_list)<1:
            final_list.append(j)
        else:
            if check_in_final(j,final_list):
                final_list.append(j)
    
    for i in final_list:
        print(i)
    print(len(final_list))

print(get_final_record(hospital_a,hospital_b))