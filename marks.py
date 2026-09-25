n=10
list=[]
count=0
total=0
for i in range(n):
    m=int(input("Enter marks"))
    list.append(m)
    total=total+m
high=max(list)
print(high)
low=min(list)
print(low)
average=total//n
print("Average",average)
for i in list:
    if i<average:
        count+=1
        print("Count students",count)
list.sort()
print("sort",list)         