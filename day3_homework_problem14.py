'''home work
1).find even or odd'''
# n=int(input())
# if n%2==0:
#     print("even")
# else:
#     print("odd")


'''2).find greatest of 3'''
# n1=int(input())
# n2=int(input())
# n3=int(input())
# if (n1>=n2) and (n1>=n3):
#     largest=n1
# elif(n2>=n1) and (n2>=n3):
#     largest=n2
# else:
#     largest=n3
# print(largest)    

        
'''3).find sum all alements in a array'''

# arr=list(map(int,input().split()))
# ans=sum(arr)
# print(ans)


'''*****IMPORTANT******'''
'''find peak element in array'''
#PRINT EVERY PEAK ELEMENT
# arr=list(map(int,input().split()))
# count=0
# for i in range(1,len(arr)-1):
#     if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
#         count=i
#         print(arr[count],end=" ")


#PRINT ONE PEAK ELEMENT    
# arr=list(map(int,input().split()))
# count=0
# for i in range(1,len(arr)-1):
#     if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
#         count=i
#         break
# print(arr[count],end=" ")


#PRINT INDEX VALUE IN WHICH PRESENT IN THE PEAK ELEMENT
# arr=list(map(int,input().split()))
# count=0
# for i in range(1,len(arr)-1):
#     if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
#         count=i
        
#         print(count,end=" ")


# for 1 2 3 4 5
arr=list(map(int,input().split()))
count=0
for i in range(1,len(arr)-1):
    if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
        count=1
if (arr[-1]>arr[-2] and arr[-1]>count):   
    count=len(arr)-1
print(arr[count])         
       

'''5).find max element in an array'''

# arr=list(map(int,input().split()))
# ans=max(arr)
# print(ans)


'''6).find 2nd max elemnt in an array'''

# arr=list(map(int,input().split()))              
# mx=max(arr[0],arr[1])                           
# secondmax=min(arr[0],arr[1])                   
# for i in range(2,len(arr)):
#     if arr[i]>mx:
#         secondmax=mx
#         mx=arr[i]
#     elif arr[i]>secondmax and mx!=arr[i]:
#         secondmax=arr[i]
# print(secondmax)            



'''7).find reverese an array without using built in functions'''

# arr=list(map(int,input().split()))
# num=[]
# j=1
# for i in arr:
#     num.append(arr[len(arr)-j])
#     j=j+1
# print(*num)    

''''8).find the sum squars of given number'''
#n=int(input())
# sum=0
# while n>0:
#     sum=sum+(n%10)*(n%10)
#     n=n//10
# print(sum)


''''9).find sum of squars of even and odd digits'''

# n=int(input())
# even=0
# odd=0

# sum=0
# while n>0:
#     if n%2==0:
#         even=(even+n)
#         even=even**2
#     else:
#         odd=(odd+n)**2
#         odd=odd**2
#         sum=even+odd 
#     n=n//10
          

#print(sum)    

'''10).check wheather polindrome or not without using reverse operation using while loop'''
# num=int(input())
# temp=num
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# if temp==rev:
#     print( "polindrome") 
# else:
#     print("not polindrome")   

'''11).write aprogram to print 1st 10 febenocci series '''

# def fib(n):
#     a=0
#     b=1
#     if n==1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c=a+b
#             a=b
#             b=c
#             print(c)

#fib(10) 
