'''prime number in traditional/square root  method'''
# a=int(input())              #a=8
# r=a**0.5                    #r=8**0.5=2.82
# count=0
# for i in range(2,int(r+1)):     #(2,int(2.82+1))=(2,3)

#     if a%i==0:               # 8%2==0  true
#         count=1               #count=1
#         break                  #break
# if count==0:
#     print("prime number")   
# else:
#     print("not prime number")     #not prime
     
'''write a program to print all the prime number in a given range '''
a=int(input())
b=int(input())
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")    



                    