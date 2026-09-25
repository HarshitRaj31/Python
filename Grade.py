n=int(input("Enter number of Subject "))
list=[]
total=0
for i in range(n):
    m=int(input("Enter marks of student"))
    list.append(m)
    total=total+m
    percentage=total/n
print("total",total)    
print("Percentage ",percentage)
for i in range(n):
    if i<=90:
        print("A+ and passed")
    elif list[i]<=89 and list[i]>=80:
         print("A and passed")
    elif list[i]<=79 and list[i]>=70:
         print("B and passed")   
    elif list[i]<=69 and list[i]>=60:
             print("B and passed")   
    elif list[i]<=59 and list[i]>=50:
             print("B and passed")                       
    elif list<50:
          print("F and Fail")         