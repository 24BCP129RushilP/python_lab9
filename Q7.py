def ispalindrome(s):
    s = ''.join(s.split()).lower()
    
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return ispalindrome(s[1:-1])

string = input("Enter a string: ")
if ispalindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")