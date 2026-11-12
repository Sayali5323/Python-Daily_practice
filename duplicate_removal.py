numbers=[]
unique_no=[]
for i in range(8):
    num=int(input("Enter the Number:"))
    numbers.append(num)

for num in numbers:
    if num not in unique_no:
        unique_no.append(num)

print("Original List:",numbers)
print("List without Duplicate:",unique_no)