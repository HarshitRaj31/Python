#2. K-Difference Pair Counter
#Count the number of distinct pairs (a,b) for which

# |a-b|=K 

#Design an O(n) expected-time solution using hashing
#meaning

arr=[1,5,3,4,2]
k=2

seen=set()

count=0
for i in arr:
    if i-k in seen:
        count=+1
    if i+k in seen:
        count+1
    seen.add(i)
    
print("Number of counts ",count)            