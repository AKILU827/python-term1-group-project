# Grade System Program

# Accept 5 marks from the user
marks = []
print("Please enter 5 marks:")

for i in range(5):
    while True:
        try:
            mark = float(input(f"Enter mark {i+1}: "))
            if 0 <= mark <= 100:
                marks.append(mark)
                i += 1
                break
            else:
                print("Please enter a mark between 0 and 100")
        except ValueError:
            print("Please enter a valid number")

# Calculate average
average = sum(marks) / len(marks)

# Determine grade based on the average
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Print results
print(f"\nMarks entered: {marks}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
