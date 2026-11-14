numbers=[2,7,11,15,3,6]
target=9
pairs=[]

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]+numbers[j]==target:
            pairs.append((numbers[i],numbers[j]))
print("Pairs:",pairs)