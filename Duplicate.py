ch=input("Enter String\n")

result=''.join(dict.fromkeys(ch))
print("after removing duplicate",result)