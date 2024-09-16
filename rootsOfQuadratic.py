import math


def roots(x, y, z):
    d = y ** 2 - 4 * x * z
    if (d < 0):
        print("No real roots exist")
    else:
        r1 = (-y - math.sqrt(d)) / (2 * x)
        r2 = (-y + math.sqrt(d)) / (2 * x)

        print(f"The roots of the equation are : {r1} and {r2}")


print('Enter the Values of the coefficients : ')
x=int(input('a= '))
y=int(input('b= '))
z=int(input('c= '))

roots(x,y,z)