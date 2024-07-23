''' GCD (greatest common divider)
GCD of two numbers 
using EUCLIDIAN ALGORITHM
''' #(%IS USED FOR REDUCING THE VALUE IN WHIE LOOP)
# a=int(input())           #5
# b=int(input())           #15
# while b!=0:               #15!=0 true              #5!=0 true      0!=0 false so it will print a value
#     a,b=b,a%b             #5,15=15 ,5%15=5         15,5=5,15%5=0 
# print(a)    

'''LCM'''
a=int(input())
b=int(input())

while b!=0:
    a,b=b,a%b
    
    a,b=b,(a*b)//a
    s=a
print(s)    