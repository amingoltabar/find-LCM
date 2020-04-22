def receive():#Function for inputting integer
    count=0
    while count==0:
        a=input('Enter the integer :')
        try:
            val=int(a)
            count+=1
            return val
        except ValueError:
            try:
                val=float(a)
                print('You entered a float. ')
            except ValueError:
                print('You did not enter a number. ')
my_list=[]
count=1
print('Creating the list')
while len(my_list)<7: #creating the list
    my_list.append(receive())
def receiveindex():#Function for inputting indexe
    count=0
    while count==0:
        a=input('Enter the index :')
        try:
            val=int(a)
            if val>=0 and val<=6:
                count+=1
                return val 
            else:
                print('Your entered index is not in range.')
        except ValueError:
            try:
                val=float(a)
                print('You entered a float. ')
            except ValueError:
                print('You did not enter a number. ')
index_list=[]
count_1=1
while len(index_list)<2: 
    index_list.append(receiveindex())
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


 
            
        
           
        
    
