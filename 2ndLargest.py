def seclar(li,x):
    li1=sorted(li)
    print(f'The second largest number is : {li1[x-2]}')

x=int(input('Enter the size of the list : '))
li=[]
for i in range(x):
    element = int(input(f'Enter the number at index {i} : '))
    li.append(element)
seclar(li,x)