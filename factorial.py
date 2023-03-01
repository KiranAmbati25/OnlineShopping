# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# a=50
# print(fact(a))
x="this is the modifiying of the version"

def fact(n):
    fact=1
    i=0
    while i<n:
        fact=fact*(i+1)
        i+=1
    return fact
a=5
print(fact(a))

def facto(n):
    fact=1
    for i in range(n):
        fact=fact*(i+1)
    return fact
b=6
print(facto(b))
