name='Harshit'
nameshort=name[0:4]
a=len(nameshort)
print("String",nameshort)
print("Length",a)
nameshort2=name[::-1]
print(nameshort2)
#Slicing
print(name[1:4:2])
print(name[-4:-1])
print(name[0:])
print(name[:4])
print(name[1:])
print(name[1:5])
#function
name3="Harshu"
print(name3.endswith("shu"))
print(name3.startswith("H"))
print(name3.capitalize())
#Escape sequence Character
new="Harshit \nis \"great\""
print(new)
#Practice
name4=input("Enter your name")
print(f"Good Afternoon,{name4}")

letter='''Dear <|Name|>,
You are Selected!
<|Date|>'''
print(letter.replace("<|Name|>","Harshit").replace("<|Date|>","13 September 2026"))

name5="Harshit  "
print(name5.find(" "))
print(name5.replace("  "," "))

letter2="Did \n\tthis match your\n intent?" #String Formating using Escape Sequence
print(letter2)