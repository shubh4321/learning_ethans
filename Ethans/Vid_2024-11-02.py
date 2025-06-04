#dictionary
#create a dynamic dictionary that will store data based on roll number given by user

d1={}
roll = int(input("Enter student's roll number: "))

d1[roll] = {}
d1[roll]['name']=input("Enter Name: ")
d1[roll]['marks']={}
d1[roll]['marks']['M']=int(input("Enter maths marks: "))
d1[roll]['marks']['C']=int(input("Enter Chemistry marks: "))
print("details",d1)