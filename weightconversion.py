weight = float(input('Enter weight : '))
print('Enter "K" for kg & "l" for Pounds ')
unit=input('Entered weight is on pounds or kg : ')

if unit.lower() =='k':
    print('Weight in pounds is '+ str(float(weight*2.20462)))
elif unit.lower()=='l':
    print('Weight in kilograms is '+ str(float(weight*0.453592)))
else: print('Invalid input')