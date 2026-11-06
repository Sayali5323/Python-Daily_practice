student={}

for i in range(3):
    subject=input("Enter the Subject:")
    marks=float(input("Enter the marks:"))
    student[subject]=marks

total_marks=0
highest=0
highest_subject=""

for subject,marks in student.items():
    total_marks=total_marks+marks
print("Total Marks",total_marks)

if marks>highest:
    highest=marks
    highest_subject=subject

avg=total_marks/len(student)
print("Average marks:",round(avg,2))

print("Highest marks",highest_subject,"-",highest)