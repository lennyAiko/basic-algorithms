# Prints any array backwards

# collect input
run = int(input("How many digits in your array?: "))

# initialize variables
values = []

# loop to carry out operation
for i in range(run):
    num = input("Enter your value: ")
    values.append(num)

# show result
print(f"The reverse of your array is: {values[::-1]}")