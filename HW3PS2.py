def main():
    s = input("Enter a string: ")
    if ispalindrome(s):
        print(s, " is a palindrome")
    else:
        print(s," is not a palindrome")
    
def ispalindrome(s):
    low = 0
    high = len(s) - 1
    while low < high:
            if s[low] != s[high]:
                return False
            low = low + 1
            high = high -1
            return True
main()

'''Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Enter a string: sock
sock  is not a palindrome
>>> '''

'''Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Enter a string: murder for a jar of red rum
murder for a jar of red rum  is a palindrome
>>> '''

