from math import floor


def bs(arr):
    dup=[]
    for elem in arr:
        dup.append(elem)

    arr.sort()
    s=int(input('Enter the element to be searched : '))
    l=0
    r=(len(arr))-1
    c = False

    while l<=r:
        m = floor((l + r) / 2)
        if s==arr[m]:
            if s in dup:
                for i in range(x):
                    if dup[i]==s:
                        print(f'The Element searched is at index : {i}')
                
            c= True
            break
        elif s > arr[m]:
            l=m+1
        else:
            r=m-1
    if not c:
        print('Element not found')

x=int(input('Enter the size of the array : '))
arr=[]
for i in range(x):
    elem=int(input(f'Enter the element at index {i} : '))
    arr.append(elem)
bs(arr)
