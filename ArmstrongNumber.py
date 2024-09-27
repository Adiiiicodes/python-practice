def arm(x,l):
    og=x
    tem2=0
    while x != 0:
        temp=x%10
        tem2=tem2 + temp**l
        x=x//10
    if tem2==og :
        print(f'{og} is an Armstrong Number')
    else:
        print(f'{og} is not an Armstrong number')

x=int(input('Enter a number : '))
l=len(str(x))
arm(x,l)
