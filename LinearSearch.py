# **** LINEAR SEARCH ITERATIVE****

'''NOTE1--->a is the array ,key is the value we are searching for'''

'''--------> for loop <---------'''

def ls(a,key):
    for i in range(len(a)):
        if a[i]==key:                               #'''TIME COMPLEXITY --> O(n)'''
            return i                               # '''SPACE COMPLEXITY --> O(1)'''
    return -1
b='this is the edited line(added)'
a=[12,34,56,78,90]
key=12
print(ls(a,key))

'''--------> while loop <--------'''

def ls(a,key):
    i=0
    while i in range(len(a)):
        if a[i]==key:                              #TIME COMPLEXITY --> O(n)
            return i                               #SPACE COMPLEXITY --> O(1)
        i+=1
    return -1
a=[12,34,56,78,90]
key=1
print(ls(a,key))

'''***** RECCURSIVE LINEAR SEARCH ******'''

'''NOTE1----> a is the array,
                i is the index which we will be incrementing by every reccursion call (max upto length of array)
                 this is very important because we will be updating it during every reccursion call to get the index of element we are searching for,     
                key is the value we are searching for!!'''

def ls(a,i,key):
    if i<len(a):
        if a[i]==key:                                  #TIME COMPLEXITY ---> O(n)
            return i                                   #SPACE COMPLEXITY ---> O(n)
        else:
            return ls(a,i+1,key)
    return -1
a=[12,34,56,78,90]
key=56
l=0
print(ls(a,l,key))

//kiran ambati
