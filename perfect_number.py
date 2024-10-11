def perfnum(x):
    main=[]
    for i in range(1,x):
        if x%i==0:
            main.append(i)
    temp=0
    for i in range(len(main)):
        temp=temp+main[i]
    if temp==x:
        print('The number entered is a PERFECT NUMBER')
    else:
        print('The number entered is not PERFECT NUMBER')

x=int(input('Enter a number to check whether it is a perfect number : '))
perfnum(x)