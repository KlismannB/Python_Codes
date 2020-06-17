array = [1,6,3,8,0,2,4,5,6,7,9,2]
changed = False
organized = False

while(not organized):
    for i in range(0,(len(array) - 1)):
        if(array[i] > array[i+1]):
            aux = array[i+1]
            array[i+1] = array[i]
            array[i] = aux
            changed = True
    if(not changed):
        organized = True 
    else:
        changed = False
        
if(len(array)%2 == 0):
    print((array[(len(array)-1)/2] + array[(len(array)-1)/2 + 1])/2)
else:
    print(array[(len(array)-1)/2])
    
array = [3, 40, 1, 2, 200, 8, 79]
changed = False
organized = False

while(not organized):
    for i in range(0,(len(array) - 1)):
        if(array[i] > array[i+1]):
            aux = array[i+1]
            array[i+1] = array[i]
            array[i] = aux
            changed = True
    if(not changed):
        organized = True 
    else:
        changed = False
        
if(len(array)%2 == 0):
    print((array[(len(array)-1)/2] + array[(len(array)-1)/2 + 1])/2)
else:
    print(array[(len(array)-1)/2])
    
array = [50, 60, 10, 30, 20, 40]
changed = False
organized = False

while(not organized):
    for i in range(0,(len(array) - 1)):
        if(array[i] > array[i+1]):
            aux = array[i+1]
            array[i+1] = array[i]
            array[i] = aux
            changed = True
    if(not changed):
        organized = True 
    else:
        changed = False
        
if(len(array)%2 == 0):
    print((array[(len(array)-1)/2] + array[(len(array)-1)/2 + 1])/2)
else:
    print(array[(len(array)-1)/2])