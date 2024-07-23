'''amstrong number'''
n=int(input())                  # n=153
s=n                              # s=153
b=len(str(n))                    # b=len(153)=3
sum1=0
while n!=0:                      #153!=0 true         15!=0 true        12!=0 true
    r=n%10                        #r=153%10=3              r=15%10=5           
    sum1=sum1+r**b               # sum1=0+3**3=27          sum1=0+5**3=125
    n=n//10                       #n=153//10=15           n=125//10=12
if s==sum1:
    print("amstrong number")
else:
    print("not amstrong number")