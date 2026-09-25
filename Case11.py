#Given a string, find the longest prefix that also occurs somewhere else in the string without overlapping the original prefix.

#Example:

s="abcabxyzabc"
ans=""

for i in range(1,len(s)+1):

    prefix=s[:i]

    if prefix in s[i:]:
        ans=prefix

print("Longest", ans)        