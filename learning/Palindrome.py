list1 = [1,2,4,2,1]

list1_copy = list1.copy()
list1_copy.reverse()
#print(list1_copy)
if(list1 == list1_copy):
    print("It's Palindrome")
else:
    print("It's not Palindrome")