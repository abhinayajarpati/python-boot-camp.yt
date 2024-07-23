'''replace the elements in array with avarage of max and min elemets'''
list=list(map(int,input().split()))
avg=0
maxi=list[0]
mini=list[0]
for i in range(len(list)):
    if list[i]>maxi:
        maxi=list[i]
    if list[i]<mini:
        mini=list[i]
avg=(maxi+mini)/2
for i in range(len(list)):
    list[i]=avg
print(list)
