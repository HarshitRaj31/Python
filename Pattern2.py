

n=5
for i in range(1,n+1):
        print("*"*i)
for i in range(n,0,-1):
        print("*"*i)      
for i in range(1,n+1):
        print(*range(1,i+1))
for i in range(1,n+1):
        print(str(i)*i)            
for i in range(n):
        print("*"*n) 
for i in range(1,n+1):
        print(" "*(n-i)+ "*"*(2*i-1))   
for i in range(n,0,-1):
        print(" "*(n-i)+ "*"*(2*i-1))    
for i in range(1,n+1):
        print(" "*(n-i)+ "".join(str(j) for j in range(1,2*i)))

for i in range(1,n+1):
        print(" "*(n-i),"*"*i)
for i in range(n,0,-1):
        print(" "*(n-i),"*"*i)  

for i in range(n,0,-1):
        print(" "*(n-i),"*"*i) 
for i in range(2,n+1):
        print(" "*(n-i),"*"*i)
 

                                                     