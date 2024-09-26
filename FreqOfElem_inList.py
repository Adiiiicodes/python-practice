from numpy.ma.core import append
def foeil(x,li):
    l2=[]

    for i in range(x):
        if li[i] not in l2:
            count = 0
            for j in range(x):
                if li[i] == li[j]:
                    count += 1
            print(f'{li[i]} occured {count} times in the given list')
            l2.append(li[i])

x= int(input('Enter the size of the list : '))
li=[]
for i in range(x):
    element=int(input(f'Enter the element at index {i} : '))
    li.append(element)
foeil(x,li)