#Program 1 — University Attendance Analysis
#A university stores the attendance percentage of N students in an array. The academic section wants
#to:
#1. Count the students whose attendance is below a given threshold.
#2. Identify the student with the lowest attendance and their position.
#3. Calculate the average attendance.

attendance = []
n = int(input("Enter number of students: "))

if n <= 0:
    print("Number of students must be greater than zero.")
else:
    for i in range(n):
        percentage = float(input(f"Enter attendance percentage for student {i + 1}: "))
        attendance.append(percentage)

    threshold = float(input("Enter threshold attendance: "))
    below_threshold = 0

    for percentage in attendance:
        if percentage < threshold:
            below_threshold += 1

    lowest = attendance[0]
    position = 0

    for i in range(1, n):
        if attendance[i] < lowest:
            lowest = attendance[i]
            position = i

    average = sum(attendance) / n

    print(f"Students below {threshold}% attendance: {below_threshold}")
    print(f"Lowest attendance: Student {position + 1} with {lowest}%")
    print(f"Average attendance: {average:.2f}%")
