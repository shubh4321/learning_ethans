# Print Hello world

# print('Hello world')
# print("Hello world Again")

# print('''Hello world
# Multiple
# line
# print''')

# String practice "Hello World"
#print string in reverse

################################

# str = "Hello World"
# print(str)
# print(str[:5])
# print('last 3 character - ', str[-3:])
# print('last 3 character in reverse - ',str[:-4:-1])
# print('All character in reverse - ',str[::-1])
# print('All except last 3 character - ',str[:len(str)-3])
# print('All except last 3 character - ',str[:-3])
# print('All except last 3 character in reverse - ',str[-3::-1])

################################
# list, tuple, set, dictionary

# l1 = [11,88.8,'Python']
# t1 = (11,88.8,'Python')
# s1 = {11,22,33,44,44,44}
# d1 = {'ID':101, 'name':'Amit','dept':'IT','mgr':'Jatin'}
# print('Reverse tuple',t1[::-1])
# print('List last 2', l1[-2:])
# print(d1['ID'],d1['mgr'])

# d1={'ID':101,'name':'Amit','marks':{'M':88,'E':66}}

# #store 2 records
# d1={'stud1':{'ID':101,'name':'Amit','marks':{'M':88,'E':66}},
#     'stud2':{'ID':101,'name':'Amit','marks':{'M':88,'E':66}}
# }
# print(d1)

# #OR
# d1={101:{'name':'Amit','marks':{'M':88,'E':66,'H':59}},
#     102:{'name':'Sumit','marks':{'M':55,'E':77,'H':78}}
# }
# print(d1[101]['name'])
# print(d1[102]['name'],d1[101]['marks']['M'],d1[102]['marks']['H'])

#############################################
#dict

d3 = {}
d3[103] = {}
d3[103]['name'] = 'Shubham'
d3[103]['add'] = 'Pune'
d3[103]['marks']={}
d3[103]['marks']={'M':76,'C':69,'E':56}
print(d3)