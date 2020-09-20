def isPalindrome(word):
    nospace = word.replace(' ','').lower()
    return nospace[::-1] == nospace

print(isPalindrome('Wół utył i ma miły tułów'))
