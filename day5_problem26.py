''' input:
hello123world
ouput:
6'''
# s=input()
# str="0123456789"
# ans=0

# for i in s:
#     if i in str:
#         ans+=int(i)
# print(ans) 

'''sum digit using ascii value'''
# inp=input()
# sum=0
# for i in inp:
#     if(ord(i)>=48 and ord(i)<=57):
#         sum+=int(i)
# print(sum)
        
'''print  capital letters in a given string'''

inp=input()

for i in inp:
    if(ord(i)>=65 and ord(i)<=90):
        
        print(i,end=" ")       
