''''prime number using half iteration method'''
n=int(input())                                   #n=7
if(n>1):                                      #7>1  true
    for i in range(2,int(n/2)+1):                 #7/2+1=4
        if n%i==0:                                 #7%2==0 false #number is prime
            print("number is not prime")
            break
        else:
            print("prime number")
else:
    print("number is not prime")            
