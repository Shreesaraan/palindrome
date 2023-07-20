def palindrome(word,start,end):
    if start>end:
        return True
    if word[start]!=word[end]:
        return False
    return palindrome(word,start+1,end-1)

word=input("Enter the word : ")
start=0
end=len(word)-1
print(palindrome(word,start,end))