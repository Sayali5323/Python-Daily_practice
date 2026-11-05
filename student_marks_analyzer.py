marks=[]
for i in range(1,6):
    mark=float(input("Enter marks for subject "))
    marks.append(mark)

sum=0
for mark in marks:
    sum=sum+mark
print("Total Marks",sum)

avg=sum/5
print("Average is:",avg)

count=0
for mark in marks:
    if mark>=40:
        count+=1
print("Student passed",count)
    