y= int(input('Enter A number : '))

def fac(x):
	if(x==0):
		return 1
		
	else:
		return x*fac(x-1)


b= fac(y)
print(f'the factorial is {b}')