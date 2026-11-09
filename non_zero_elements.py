numbers=[0,5,0,3,8,0,2]
result=[]

for i in numbers:
    if i>0:
        result.append(i)

for i in numbers:
    if i==0:
        result.append(i)

print("Original List",numbers)
print("Updated List",result)