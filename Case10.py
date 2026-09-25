#4. Maximum Number of Non-overlapping Meetings
#Each meeting is represented by (start,end). Select the maximum number of meetings such that none overlap.

#Instead of memorizing the greedy rule, prove why selecting the appropriate meeting first is safe.

meetings = [
    (1, 3),
    (2, 4),
    (3, 5),
    (5, 7),
    (6, 8)
]

# Sort according to ending time
meetings.sort(key=lambda x: x[1])

count = 0
last_end = 0

for start, end in meetings:

    if start >= last_end:
        print("Selected:", (start, end))
        count += 1
        last_end = end

print("Maximum meetings:", count)