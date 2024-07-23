'''find the  element that is  present in k+n index  k is given by user
input foramt
k=3
n=2
3 6 8 4 61 2
output=2
example2
k=3
n=4
70 54 36 72
output=error'''
# n=int(input())
# k=int(input())
# list=list(map(int,(input().split())))
# s=len(list)
# if s<k+n:
#     print("error")
# else:
#     for i in range(len(list)):
#         print(list[k+n])
#         break
'''important question
print the element in a particular index(cyclic printing)
input foramt: 1 2 3 4 5
k=8
output:4'''
k=int(input())
list=list(map(int,input().split()))                      #k=14   index=2
                                                          #70 30 54 34 35 65 
for i in range(1,len(list)):                             # 0   1  3  4  5  6  
    if len(list)<k:                                    #   7  8  9  10  11 12
        p=k%len(list)                                  # 13 14
        index=p
print(index)
print(list[index])
        
        





