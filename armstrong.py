n=153
s=0
q=n
while(n!=0):
 r=n%10
 s=s+r*r*r
 n=n//10

if q==s :
 print("armstrong")
else:
  print("not armstrong")