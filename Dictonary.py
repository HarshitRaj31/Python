marks={"Harshit":100,
       "Sristi":99}
print(marks,type(marks))
print(marks["Harshit"])
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Sristi":98})
print(marks)
print(marks.get("Harshit"))
#Problem
words={"Madad":"Help",
       "Harshit":"Joy"}
word=input("Enter ")
print(words[word])

d={}
name=input("Enter name")
lang=input("enter language")

d.update({name:lang})
name=input("Enter name")
lang=input("enter language")

d.update({name:lang})

