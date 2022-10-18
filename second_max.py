# checks for the second largest number in an array

# collect input
run = int(input("How many digits in your array?: "))

# initialize variables
values = []
max = 0
subtracted_value = 0
chosen = 0
second_max = 0

# loop to carry out operation
for i in range(run):
    num = int(input("Enter your value: "))
    values.append(num)

## get the max value first
for x in range(len(values)):
    if max == 0:
        max = values[x]
    if max < values[x]:
        max = values[x]

for y in range(len(values)):
    if max == values[y]:
        continue
    else:
        num = max - values[y]
        if subtracted_value == 0:
            subtracted_value = num
        if subtracted_value > num:
            subtracted_value = num
            second_max = values[y]

# show result
print(f"The second largest value in the array is: {second_max}")
