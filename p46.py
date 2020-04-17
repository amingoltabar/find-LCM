my_list=[]
count=1
print('Creating the list')
while len(my_list)<7: #creating the list
    print('Enter the integer number',count,end='')
    a=input(':')
    try:
        val=int(a)
        my_list.append(val)
        count+=1
    except ValueError:
        try:
            val=float(a)
            print('You entered a float')
        except ValueError:
            print('You did not enter a number. ')
index_list=[]
count_1=0
while len(index_list)<2: #inputting indexes
    print('Enter the index number',count_1+1,end='')
    b=input(':')
    try:
        val=int(b)
        if val<=6 and val>=0:
            index_list.append(val)
            count_1+=1
        else:
            print('Your entered number is not in range.')
    except ValueError:
        try:
            val=float(b)
            print('You entered a float.')
        except ValueError:
            print('You did not enter a number.')
def findLCM(x,y,array):#This function receives 2 indexes and calculates the LCM of their elements.
    i=1
    while True:
        if i%array[x]==0 and i%array[y]==0:
            LCM=i
            break
        i+=1
    return LCM
x=index_list[0]
y=index_list[1]
answer=findLCM(x,y,my_list)
print('LCM of index',x,'and index',y,'elements :',answer)


 
            
        
           
        
    
