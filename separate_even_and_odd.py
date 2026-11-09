numbers=[]
even_no=[]
odd_no=[]

for i in range(1,11):
    num=int(input("Enter the no:"))
    numbers.append(num)

for i in numbers:
    if i%2==0:
        even_no.append(i)
    else:
        odd_no.append(i)

print("Even No:",even_no)
print("Odd No:",odd_no)