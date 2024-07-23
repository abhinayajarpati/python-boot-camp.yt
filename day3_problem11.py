'''print minimum element in given list'''
list=list(map(int,input().split()))

mini=list[0]
for i in range(len(list)):
    if list[i]<mini:
        mini=list[i]
print(mini)