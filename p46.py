my_list=[]
for i in range(7):#creating the list
    a=float(input('Create your list.Enter the integer: '))
    while a!=int(a):
        a=float(input('You did not enter an integer.Enter the integer: '))
    a=int(a)
    my_list.append(a)
x=float(input('Enter the  index: '))
while x<0 or x>6 or x!=int(x):#Entered indexes must be integer and in the range of the list.
    x=float(input('Index you have entered is out of range or non-integer.Enter the index again: '))
x=int(x)
y=float(input('Enter the  index: '))
while y<0 or y>6 or y!=int(y):
    y=float(input('Index you have entered is out of range or non-integer.Enter the index again: '))
y=int(y)
def findLCM(x,y,array):#This function receives 2 indexes and calculates the LCM of their elements.
    i=1
    while True:
        if i%array[x]==0 and i%array[y]==0:
            LCM=i
            break
        i+=1
    return LCM
answer=findLCM(x,y,my_list)
print('LCM of index',x,'and index',y,'elements :',answer)


 
            
        
           
        
    
