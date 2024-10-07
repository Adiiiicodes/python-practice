import math
def med(arr):
    arr.sort()
    if x%2==0 :
        medi = (len(arr) / 2)
        mod1=math.floor(medi)
        mod3=mod1+1
        avg=(arr[mod1]+arr[mod3])/2
        #print(avg)
        print(f'{avg} is the median ')
    else :
        medi = (len(arr) / 2)
        mod2=math.floor(medi)
        #print(mod2)
        print(f'{arr[mod2]} is the median ')

x=int(input('Enter the number of elements in the list : '))
arr=[]
for i in range(x):
    ele=int(input(f'Enter the element at index {i} : '))
    arr.append(ele)
med(arr)