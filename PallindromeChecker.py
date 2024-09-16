x = input("Enter A string to check whether it is a palindrome or not :  ")
s=0
e = len(x) - 1
while s<e:
    if x[s] != x[e] :
        print("Not a Palindrome")
        s+=1
        e-=1
        break
    else:
        print('It is a palindrome')
        break