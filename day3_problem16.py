'''find the duplicants in array
8 7 7 8 5 4 4 8 9'''
#lst=list(map(int,input().split()))
# li1=[]

# for i in lst:
    
#     if (i not in li1):
#         li1.append(i)
# print(li1)  

'''print duplicants in array using stack '''
lst=list(map(int,input().split()))
li1=[]
for i in lst:
    
    if (i in li1):
        li1.append(i)
print(li1) 