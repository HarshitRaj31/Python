code=input("Enter the code:")
valid=True

for i in range(3):
    if not("A"<=code[i]<="Z"):
        valid=False
        break

if valid:
   if code[3]!="-":
      valid=False

if valid:
    for i in range(4,8):
        if not("0"<=code[i]<="9"):
            valid=False
            break

if valid:
    if code[8]!='-':
        valid=False

if valid:
    for i in range(9,12):
        if not("0"<=code[i]<="9"):
            valid=False          
            break

if len(code)!=12:
    valid=False              

print("Valid code")



