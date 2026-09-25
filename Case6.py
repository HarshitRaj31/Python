list=[]
n=int(input("Enter number of products: "))
for i in range(n):
    name=input("Enter product name: ")
    price=int(input("Enter product price: "))
    list.append((name,price))
print("product lists are",list)    

for name,price in list:
    print(sorted(list,key=lambda x:x[1]))
    print(price)

bubble_sort=list.copy()

for i in range(n-1):
    for j in range(n-i-1):
        if bubble_sort[j]>bubble_sort[j+1]:
            temp=bubble_sort[j]
            bubble_sort[j]=bubble_sort[j+1]
            bubble_sort[j+1]=temp

selection=list.copy()

for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if selection[j]<selection[min]:
            min=j
    if min!=i:
        temp=selection[i]
        selection=selection[min]
        selection[min]=temp

insertion=list.copy()        

for i in range(1,n):
    current=insertion[i]
    prev=i-1
    while prev>=0 and insertion[prev]>current:
          insertion[prev+1]=insertion[prev]
    insertion[prev+1]=current  
          