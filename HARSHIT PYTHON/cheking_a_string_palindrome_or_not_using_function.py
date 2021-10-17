def is_palindrome(word):
    rev_word=word[::-1]
    if rev_word==word:
        return 'it is a palindrome'
    else:
        return 'it is not a palindrome'
    
    
print(is_palindrome('mani'))
    