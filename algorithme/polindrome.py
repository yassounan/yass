def checkPalindrome(word):
    n=len(word)
    is_Palindrome=True

    for i in range(n//2):
        if word[i] != word[n-i-1]:
            is_Palindrome=False
    if is_Palindrome:
        print(word,"is palindrome")
    else:
        print(word,"is not palindrome")
word=str(input("put a word : "))
checkPalindrome(word)