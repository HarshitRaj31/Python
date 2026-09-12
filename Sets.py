set1={1,2,32}
print(set1)
# empty=set() #Empty set

s={1,22,22,44}
print(s)
s.add(23)
print(s)

s.remove(22)
print(s)
s1={1,3,4,5}
s2={2,6,7,8}
print(s1.union(s2))
print(s1.intersection(s2))
#problem
s3=set()
n=input("Enter no.")
s3.add(int(n))
n=input("Enter no.")
s3.add(int(n))
n=input("Enter no.")
s3.add(int(n))
n=input("Enter no.")
s3.add(int(n))
print(s3)

s4=set()
s4.add(18)
s4.add("18")
print(s4)

s5=set()
s5.add(20)
s5.add('20')
print(len(s5))

#change value of list in set
s6={8,7,12,"Harry",[1,2]}
#list cannot be inside set
