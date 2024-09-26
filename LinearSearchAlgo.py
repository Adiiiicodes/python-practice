def lsa(x,li,y):
    for i in range(x):
        if li[i]==y :
            print(f'The element you are searchng is found at index {i}')
        else :
            print('No match found')

x=int(input('Enter the size of the list : '))
li=[]
for i in range(x):
    element=int(input(f'Enter the element at index {i} : '))
    li.append(element)

y=int(input('Enter the Element to be searched : '))
lsa(x,li,y)
