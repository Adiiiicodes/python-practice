def find_mode(arr):
    frequency = {}


    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1


    max_count = 0
    mode = None
    for key in frequency:
        if frequency[key] > max_count:
            max_count = frequency[key]
            mode = key

    return mode


x = int(input('Enter the number of elements required inside the list: '))

numbers = [0] * (x)

print('Enter the elements:')

for i in range(0, x):
    number=int(input())
    numbers[i] = number


print("Mode of the list is:", find_mode(numbers))

