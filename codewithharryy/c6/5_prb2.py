subject1 = int(input("Enter the marks: "))
subject2 = int(input("Enter the marks: "))
subject3 = int(input("Enter the marks: "))

total_per = (100 * (subject1 + subject2 + subject3)) / 300

if total_per >= 40:
    print("Pass", total_per)
else:
    print("Fail", total_per)