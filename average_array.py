### Gives the average of an array

def average_array(array):

    length_array = len(array)

    sum = 0

    for i in array:
        sum += i
    
    average = sum/length_array

    return average

values = [2, 3, 4, 5]

get_average = average_array(values)

print(f'The average of {values} is: {get_average}')