books=[]
n=1
for i in range(n):
    id=int(input("Enter Book Id "))
    title=input("Enter book name")
    author=input("Enter Author name")
    Publication=int(input("Enter publication year "))
    book=(id,title,author,Publication)

    books.append(book)

search = int(input("Enter Id "))

for i in books:

    if i[0] == search:
        print("Book ID:", i[0])
        print("Title:", i[1])
        print("Author:", i[2])
        print("Publication Year:", i[3])
        print("Book found")
        break

else:
    print("Book not found")
