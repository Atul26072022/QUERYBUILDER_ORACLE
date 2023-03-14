from django.test import TestCase

# Create your tests here.
l1 = ['ID', 'X', 'Y', 'Z']

# l2 = ['ID', 'X', 'Y', 'Z','R']
l3 = []

dict2 = {
    "TableName" : "qqabc",
    "Coloumn" : {
        "a" : "x",
        "b" : "y",
        "c" : "z",
        'd' : 'g'
    }
}

for i in dict2['Coloumn'].values():
    if i.upper() in l1:
        continue
    else:
        l3.append(i)

print(l3)