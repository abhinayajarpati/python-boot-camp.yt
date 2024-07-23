'''sum of digits
1+2+3'''
n=int(input())
sum=0

while (n>0):
    a=n%10
    sum=sum+a  #IMPORTANT STATMENT
    n=n//10
    
print(sum)     

