# ***** BINARY SEARCH ****

'''NOTE1--->a is the array ,
            key is the value we are searching for'''

def bs(a,key):
    low=0
    high=len(a)-1                                   # TIME COMPLEXITY --> O(logn)
    while low<=high:                                # SPACE COMPLEXITY --> O(1)
        mid=int((low+high)//2)
        if a[mid]<key:
            low=mid+1
        elif a[mid]>key:
            high=mid-1
        else:
            return mid
    return -1
a=[12,32,45,56,67,78,89]
k1=32
k2=12
k3=78
k4=45
k5=89
k6=10
print(bs(a,k1))
print(bs(a,k2))
print(bs(a,k3))
print(bs(a,k4))
print(bs(a,k5))
print(bs(a,k6))


# **** RECCURSIVE BINARY SEARCH ****

'''NOTE2 ----> a is the array,
               low and high are the indexes of the first and last two elements of the array 
                    ((low and high are very important because during every reccursion call we will be changing(updating) them 
                    and finally get the index of the element we are searching for,
               key is the element we are searching for))'''

def bs(a,low,high,key):
    if low<=high:
        mid=int((low+high)//2)
        if a[mid]==key:                             # TIME COMPLEXITY ---> O(logn)
            return mid                              # SPACE COMPLEXITY ---> O(logn)
        elif key<a[mid]:
            return bs(a,low,mid-1,key)
        else:
            return bs(a,mid+1,high,key)
    else:
        return -1
a=[12,32,45,56,67,78,89]
low=0
high=len(a)-1
k1=32
k2=12
k3=78
k4=45
k5=89
k6=10
print(bs(a,low,high,k1))
print(bs(a,low,high,k2))
print(bs(a,low,high,k3))
print(bs(a,low,high,k4))
print(bs(a,low,high,k5))
print(bs(a,low,high,k6))
