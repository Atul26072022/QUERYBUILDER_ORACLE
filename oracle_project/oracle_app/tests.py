from django.test import TestCase

# Create your tests here.
l1 = ['ID', 'X', 'Y', 'Z']

l2 = ['ID', 'X', 'Y', 'Z','R']
l3 = []
l4 = ['ID']
dict2 = {
    "TableName" : "qqabc",
    "Coloumn" : {
        "a" : "g",
        "c" : "z",
        'd' : 'x'
    }
}

for i in dict2['Coloumn'].values():
    l4.append(i.upper())
    if i.upper() not in l1:
        l3.append(i)
    # else:
    #     l5 = [x for x in l1 if x not in ]
 
l5 = [x for x in l1 if x not in l4 ]
print(l5)
   


     
# print(l3)
# print(l4)
