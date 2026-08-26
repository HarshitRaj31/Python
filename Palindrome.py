n=121
s=0
q=n
while(q!=0):
 r=q%10
 s=s*10+r
 q=q//10

if n==s :
 print("palindrome")
else:
  print("not palindrome")