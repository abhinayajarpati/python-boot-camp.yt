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