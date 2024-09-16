def fibo(x):
    prev = 0
    cur = 1
    temp=2

    while temp<x:
        next = prev + cur
        prev = cur
        cur = next
        print(next)
        temp+=1

x=int(input("Enter the number of terms required : "))

print(0)
print(1)
if x>2:
    fibo(x)

