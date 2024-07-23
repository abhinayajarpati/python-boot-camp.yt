'''friendly number'''
n1=int(input())
n2=int(input())
sum1=0
sum2=0
for i in range(1,n1):
    if n1%i==0:
        sum1=sum1+i
for i in range(1,n2):
    if n2%i==0:
        sum2=sum2+1
if(sum1==n1 and sum2==n2):
    print("friendly number")
else:
    print("not friendly number")