#conditionals Statements,loops and Strings
''''
#EVEN & ODD NUMBER

num=int(input("Enter the Number: "))
if num%2==0:
    print("Even NO")
else:
    print("Odd NO")

#SUM OF NATURAL NO

total=0
n=int(input("Enter the positive number: "))
for i in range(1,n+1):
    total=total+i
print(total)
'''

#COUNT VOWELS IN A STRING

word=input("Enter the word: ")
count=0
for letter in word:
    if letter in "aeiouAEIOU":
        count+=1
print("Number of vowels",count)