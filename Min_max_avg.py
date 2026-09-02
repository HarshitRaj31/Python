number=[]
n= int(input("Enter number\n"))
for i in range(n):
    m=int(input("Enter a number"))
    number.append(m)
    print("List",number)

    avg=sum(number)/len(number)
    maximum=max(number)
    minimum=min(number)
    print("Average",avg)
    print("maximum",maximum)
    print("minimum",minimum)
    