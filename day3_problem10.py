'''find the maximum element in a given list

sample input:
test case0= 12 23 36 44 45 57
57
-----------
test case1= 56 78 -8 12 34 -99
------------
'''
list=list(map(int,input().split()))
#print(max(list))
maxi=list[0]
for i in range(len(list)):
    if list[i]>maxi:
        maxi=list[i]
print(maxi)
    


