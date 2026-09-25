#6. Exactly K Distinct Values
#Count the number of subarrays containing exactly K distinct integers.

#Try deriving the solution from Exactly(K) = AtMost(K)-AtMost(K-1)

def atMost(arr, k):

    if k == 0:
        return 0

    left = 0
    count = 0
    freq = {}

    for right in range(len(arr)):

        # Add current element
        freq[arr[right]] = freq.get(arr[right], 0) + 1

        # Too many distinct values
        while len(freq) > k:

            freq[arr[left]] -= 1

            if freq[arr[left]] == 0:
                del freq[arr[left]]

            left += 1

        # Number of valid subarrays ending at right
        count += right - left + 1

    return count


arr = [1, 2, 1, 2, 3]
k = 2

answer = atMost(arr, k) - atMost(arr, k - 1)

print("Number of subarrays:", answer)