def is_palindrome(num):
    return str(num) == str(num)[::-1] # [::-1] make the string in reverse order

number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindromic number.")
else:
    print(f"{number} is not a palindromic number.")
