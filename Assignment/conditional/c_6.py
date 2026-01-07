# Get input from user and display if the string is palindrome

text = input("Enter a string: ")

if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is NOT a palindrome.")
