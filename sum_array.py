### Gives the sum of an array

def sum_array(array):

    sum = 0

    for i in array:
        sum += i

    return sum

values = [2, 3, 4, 5]

get_sum = sum_array(values)

print(f'The sum of {values} is: {get_sum}')