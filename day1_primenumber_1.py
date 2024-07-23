'''prime number in square root method'''
import math
n=int(input())                                       #n=7
for i in range(2,int(math.sqrt(n))+1):               #i=2,sqrt(7)=
    if n%i==0:
        print("not prime number")
    else:
        print("prime number")
