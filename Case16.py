
n=2
total = 0
for i in range(n):
    book=int(input("Enter number of books"))
    if book>20:
     print("Issued")

    total=total+book
average=total//n
print("Average ",average)
