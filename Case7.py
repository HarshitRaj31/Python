#1. Longest Subarray with Equal Odd and Even Counts
#Given an array, find the length of the longest contiguous subarray containing the same number of odd and even elements.

#Example:

#[2, 5, 7, 4, 6, 9]

#Think about converting one category to +1 and the other to -1.

arr=[2,5,7,4,6,9]
prefix=0
first={0:-1}
max_len=0

for i in range(len(arr)):
    if arr[i]%2==0:
        prefix=+1
    else:
        prefix=-1

    if prefix in first:
       length= i-first[prefix]

       if length>max_len:
           max_len=length
    else:
        first[prefix]=i       

print("Length",max_len)
