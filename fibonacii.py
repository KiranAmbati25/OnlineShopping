nag="this is modified...."

def fibo(n):
    a=0
    b=1
    i=0
    print(a)
    # print(b)
    while i<n:
        c=a+b
        print(c)
        a=b
        b=c
        i+=1
    
fibo(8)

# def fiboo(n): ------------------------------> This is reccursive approach
#     if n==0:
#         return 0   
#     elif n==1:
#         return 1
#     else:
#         return fiboo(n-1)+fiboo(n-2)

# print(fiboo(8))
