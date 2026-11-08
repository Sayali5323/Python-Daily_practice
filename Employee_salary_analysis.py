#Employee salary analysis

salaries={
    "Asha":35000,
    "Ravi":45000,
    "Neha":40000,
    "Pratik":50000,
}
total=0
for name,score in salaries.items():
    total=total+score
print("Total of Salaries:",total)
avg=total/len(salaries)
print("Average:",avg)

print("Above average")
for name,score in salaries.items():
    if score>=avg:
        print(name)

