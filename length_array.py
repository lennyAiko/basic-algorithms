### GET THE LENGTH OF AN ARRAY

def get_length(values):

    count = 0

    for i in values:
        count += 1
    
    return count

values = [2, 3, 4, 5]

array_length = get_length(values)

print(f'The length of {values} is {array_length}')