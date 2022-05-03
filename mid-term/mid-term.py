from cmath import sqrt
from operator import indexOf


a = [1,2,3,4,3,6,7,8,9]

j = 0
while j < 11:
    print(a[j])
    j+=4

print(a.index(3))

a = "14"
b= str(15)
c= a+b
print(c)

num = (5+4)

num = num/9
num *=2
print(num)


N = "happy birth"
V = "aeiou"

j = 0
l = len(N)
c = 0
while j < l:
    if N[j] in V:
        c +=1
    j+=1
print(str(c))

l = None 

def calsum(L):
    return L[0] + calsum(L[2:])

j = 4
while j < 55:
    j+=3

print(j)

a = 4**2
print(a)

def fi(n):
    if n in [0,1]:
        return n
    else:
        return fi(n-1) + fi(n-2)

print(fi(5))

l = (1,2,3)
print(indexOf(l,5))