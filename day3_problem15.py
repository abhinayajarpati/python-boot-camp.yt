'''find the missing number in an array
input foramt:
1 2 3 4 6 7 
missing number:5'''
list1=list(map(int,input().split()))
n=int(input())
t=n*(n+1)/2
sum=0
mis=0
for i in range(len(list1)):
    sum+=list1[i]
mis=t-sum    
print(sum) 
print(mis)   
               

     