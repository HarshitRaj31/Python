A={"Cosmetics","Food","Shoes"}
B={"Food", "Shoes", "Books"}
C = {"Cosmetics", "Books", "Toys"}
D = {"Food", "Toys", "Shoes"}
common =A&B
print("Product purchase by both customer",common)

print("Product purchase by customer A",A)
print("Product purchase by customer D ",D)

either= A|B|C|D

print("Product purchase by both customer",either)