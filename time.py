import time
timestamp = int(time.strftime('%H'))

if(timestamp<12):
	print('Good morning')
	
elif(timestamp>12 and timestamp<15):
	print('Good afternoon')
 

elif(timestamp>15 and timestamp<21):
	print('Good Afternoon')
	
else:
	print('Good Night')

