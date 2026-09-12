list=["Apple","Orange",5,345.06,False,"Harshit"]
print(list)
print(list[3])
list[0]="Grapes"
print(list)
print(list[0:4])
#Methods
list.append("Hello")
print(list)
l1=[1,4,2,6,3]
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.insert(2,9)
print(l1)
l1.pop(2)
print(l1)

# Problem
fruits=[]
f1=input("Enter fruits")
fruits.append(f1)
f2=input("Enter fruits")
fruits.append(f2)
f3=input("Enter fruits")
fruits.append(f3)
f4=input("Enter fruits")
fruits.append(f4)
print(fruits)

marks=[2,4,1,5]
marks.sort()
print(marks)