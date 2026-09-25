#8. Nearest Greater on Both Sides
#For every element, find its nearest greater element on the left and nearest greater element on the right.

#Target complexity: O(n).

#The central concept is the monotonic stack.

arr = [2, 1, 5, 3, 4]

left = [-1] * len(arr)
stack = []

for i in range(len(arr)):

    while stack and stack[-1] <= arr[i]:
        stack.pop()

    if stack:
        left[i] = stack[-1]

    stack.append(arr[i])

print("Nearest greater on left:")
print(left)