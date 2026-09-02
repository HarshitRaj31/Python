list=[]
n=int(input("Enter Number of Elements\n"))
for i in range(n):
    m=int(input("Enter a number"))
    list.append(m)
print("number",list)

search=int(input("Enter Element"))

if search in list:
    print("Found")
    print("Count",list.count(search))
else:
    print("none")