def longest_equal_odd_even_subarray(numbers):
    """Return the length of the longest subarray with equal odd/even values."""
    first_seen = {0: -1}
    balance = 0
    longest = 0

    for index, number in enumerate(numbers):
        balance += 1 if number % 2 == 0 else -1

        if balance in first_seen:
            longest = max(longest, index - first_seen[balance])
        else:
            first_seen[balance] = index

    return longest


numbers = [2, 5, 7, 4, 6, 9]
print(longest_equal_odd_even_subarray(numbers))  # 6
