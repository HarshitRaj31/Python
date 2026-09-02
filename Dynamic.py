number=[]
n= int(input("Enter number\n"))
for i in range(n):
    m=int(input("Enter a number"))
    number.append(m)
    print("List",number)

    name= int(input("Enter number\n"))
    number.append(name)

    print("List",number)
    search=int(input("Enter Element"))

if search in number:
    print("Found")
    print("Count",number.count(search))
else:
 print("Not found")   

remove=int(input("Enter Element"))
    
if remove in number:
        print("Found")
        print("Count",number.remove(remove))

else:
        print("Not found")   

        print("Updated student",number)