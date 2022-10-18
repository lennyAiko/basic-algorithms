# an algorithm to search for min and max numbers in an array

# initialize array or collect user input
run = int(input("How many digits?: "))

# initialize variable
values = []
min = 0

# loop to perform operation
for i in range(run):
    num = input("Enter your value: ")
    values.append(num)

for i in range(len(values)):
    if min == 0:
        min = values[i]
    if min > values[i]:
        min = values[i]

# show result
print(min)