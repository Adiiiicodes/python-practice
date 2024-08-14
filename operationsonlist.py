listt = []


def condition(y):
    match y:
        case 1:
            a = int(input('Enter the number of elements to add to the list: '))
            for i in range(a):
                x = int(input(f'Enter element {i + 1}: '))
                listt.append(x)
            print(f'Elements added. Current list: {listt}')

        case 2:
            if listt:
                c = int(input('Enter the element to be deleted: '))

                if c in listt:
                    listt.remove(c)
                    print(f'Element {c} deleted. Current list: {listt}')
                else:
                    print(f'Element {c} not found in the list.')
            else:
                print('List is empty. Nothing to delete.')

        case 3:
            print(f'The current list is: {listt}')

        case 4:
            print('Exiting the program...')
            return True

        case _:
            print('Invalid choice. Please enter a valid number.')
            return False


while True:
    print('******** Enter the operation *********')
    y = int(input('1. Insert \n2. Delete \n3. Display \n4. Exit \n'))

    if condition(y):
        break



