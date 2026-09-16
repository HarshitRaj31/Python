list=[]

n=int(input("Enter no. Patient  "))
for i in range(n):
    m=input("Enter Patient ID ")
    list.append(m)
    print(list)
    set1=set(list)

print(set1)
print("Adding an element")

set1.add(5)
print(set1)

print("Removing an element")
set1.discard(2)
print("new Set",set1)
