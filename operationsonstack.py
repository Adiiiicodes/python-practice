

top =-1
max = 10
st = [max]


def display():
    if(top==-1) :
        print('Error : Stack is empty')
    else :
        print('The Elements in Stack are :')
        for i in range(0, max-1):
            print(f'{st[i]}')


def peek(top):
    if(top==-1):
        print("Error : Stack is Empty")
    else :
        print(f"Element on the top is {st[top]}")


def pop(top):
    if(top==-1):
        print('Error : StackUnderflow ')
    else :
        print(f"Poped Element is : {st[top]}")
        top=top-1



def push(top):
    item=int(input('Enter a Number : '))
    if(top==max-1):
        print("Error : StackOverflow")
    else:
        top=top+1
        st.append(item)



while True :

    print('********Main Menu********')
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. Display')
    print('5. Exit')

    x = int(input("'Enter You'r Option : "))
    match x:
        case 1:
            push(top)
            break

        case 2:
            pop(top)
            break

        case 3:
            peek(top)
            break

        case 4:
            display()
            break






