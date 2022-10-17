# Check for palindrome in text and number

# ask user choice
from email import message


print("""
    Welcome to palindrome checker.
""")

user_input = input("Enter input: ")

# create functions

## function for text
def palindrome_checker(user_input):
    split_text = []
    counter = 0
    for i in user_input:
        split_text.append(i)
    
    cup = split_text[::-1]

    for x in range(len(split_text)):
        if split_text[x] != cup[x]:
            counter = 1
    
    if counter == 0:
        message = "a palindrome"
        return message
    else:
        message = "not a palindrome"
        return message


# show result

result = palindrome_checker(user_input)

print(f"The input is {result}")