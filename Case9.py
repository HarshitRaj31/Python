#3. Remove One Element for Strict Increase
#Determine whether an array can become strictly increasing after removing at most one element.

#Example:

#[1, 2, 6, 4, 5] → true.

#The difficult part is deciding which element should be removed when a violation occurs

def can_be_strictly_increasing(numbers):
    """Return True when removing zero or one item makes *numbers* increase."""
    removals = 0

    for index in range(1, len(numbers)):
        if numbers[index] <= numbers[index - 1]:
            removals += 1
            if removals > 1:
                return False

            # At a violation such as 6, 4, either value can be removed.
            # Keep 4 only if it also fits after the value before 6.
            if index > 1 and numbers[index] <= numbers[index - 2]:
                # Treat the current value as removed for later comparisons.
                numbers[index] = numbers[index - 1]

    return True


# A copy is used because the function may temporarily replace one value.
arr = [1, 2, 6, 4, 5]
print(can_be_strictly_increasing(arr.copy()))  # True
