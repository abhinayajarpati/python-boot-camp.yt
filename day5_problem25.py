'''check how ,any owels there in string'''

# list=['a','e','i','o','u']
# abc="bcdfghjklmnpqrstvwxyz"
# count1=0
# count2=0
# p=input()
# s=p.lower()

# for i in s:

    
#     if i in list:
#         count1+=1
#     elif i  in abc:
#         count2+=1 

# print("number of owels are",count1)
# print("number of consonantes are",count2)


'''print the all owels follwed by consonantes'''
#hello world----->eoohllwld


list=['a','e','i','o','u']
abc="bcdfghjklmnpqrstvwxyz"
p=input()
s=p.lower()
ans1=0


for i in s:

    
    if(i in list):
        print(i,end="")

for i in  s:
    if i in abc:
        print(i,end="")
            
