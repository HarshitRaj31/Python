dic=[{"Name":"Harshit","Course":"python"},
     {"Name":"Harshit","Course":"UDB"},
     {"Name":"Ankita","Course":"python"},
     {"Name":"Ayan","Course":"AI"}]

count = {}

for student in dic:
    name = student["Name"]
    if name in count:
        count[name] += 1
    else:
        count[name] = 1

for name in count:
    if count[name] == 2:
        print(name)

for students in dic:
    if students["Course"]=="python":
        print(students["Name"])

for students in dic:
    if students["Course"]=="AI":
        print(students["Name"])     

for student in dic:
    name = student["Name"]
    if name in count:
        count[name] += 1
    else:
        count[name] = 1

for name in count:
    if count[name]>=1:
        print(name)           