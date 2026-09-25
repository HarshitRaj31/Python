dic={}
n=int(input("Enter number of products "))

history = []

while True:
    choose=int(input("Enter the option"))
    print("\n1. Add Product")
    print("2. View Products")
    print("3. Remove Product")
    print("4. Exit")
    match choose:
     case 1:
        print("Add a new product")
        for i in range(n):
            Product_code=input("Enter product code")
            Name=input("Enter name of product ")
            price=input("Enter price")
            quantity=input("Enter quatity of stock")
            dic[Product_code]={
            "Name":Name,
            "Price":price,
            "quantity":quantity
            }
            
     case 2:
        print("Sell a product")
        p=input("Enter the product")
        if p in dic:
           history.append(p)
           del dic[p]
        
     case 3:
        print("View full inventory ")
        print(dic)

     case 4:
        print("view history")
        for key, value in dic.items():
         print(key, value)        

     case _:
            print("Invalid input")
            break
        