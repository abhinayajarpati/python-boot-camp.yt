num=int(input())  #121
reverse=0
i=num        #i=121
while(num>0):   #121>0 true
    reverse=reverse*10+num%10    #0*10+121%10=1   #1*10+12%10=12    12*10+1%10=121
    num=num//10                  #121//10=12      #12//10=1           #1//10=0
if(i==reverse):                #121=121
    print("it is polindrome")
else:
    print("it is not polindrome")