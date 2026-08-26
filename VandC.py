s=input("Enter your String")
v=0
c=0
for ch in s:
    if ch in"aeiouAEIOU":
     v=v+1
    elif (ch.isalpha()):
       c=c+1

print("consonent",c)
print("Vowel",v)
