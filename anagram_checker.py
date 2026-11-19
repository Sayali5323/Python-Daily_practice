#ANAGRAM -- Two words are anagrams if they contain exactly the same letters with the same frequency,but in a different order.

def check_anagram(word1,word2):
    dict1={}
    dict2={}

    for char in word1:
        if char in dict1:
            dict1[char]+=1
        else:
            dict1[char]=1

    for char in word2:
        if char in dict2:
            dict2[char]+=1
        else:
            dict2[char]=1         

    if dict1==dict2:
        return True
    else:
       return False


word1=input("Enter the 1st Word:").lower()
word2=input("Enter the 2nd Word:").lower()

result=check_anagram(word1,word2)
if result:
    print(word1,"and",word2,"are anagrams.")
else:
    print(word1,"and",word2,"are not anagrams.")