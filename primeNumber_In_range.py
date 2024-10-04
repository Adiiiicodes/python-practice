def pmn(i):
    if i<=1:
        print(f'{i} is not a prime number')
    elif i==2 :
        print(f'{i}')
    else :
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(f'{i} ')


def pnir(x,y):
    for i in range(x,y+1):
        pmn(i)


x=int(input('Enter the lower limit of the range : '))
y=int(input('Enter the upper limit of the range : '))
i=1
if x>y:
    print('Enter a valid input')

else:
    pnir(x, y+1)
