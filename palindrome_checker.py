
def is_palindrome(text):
    cleaned=text.lower().replace(" ","")#to remove spaces between sentence

    for i in range(len(cleaned)//2):#divided by 2 becoz we want to compare half string with half
        if cleaned[i]!=cleaned[len(cleaned)-1-i]:
            return False
    return True

text=input("Enter the sentence or word:")
if is_palindrome(text):
    print(text,"is a palindrome")
else:
    print(text,"is not a palindrome")