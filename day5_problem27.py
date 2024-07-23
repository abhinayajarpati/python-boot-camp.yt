'''print the unique charachters in a string'''
list=['a','e','i','o','u']
abc="bcdfghjklmnpqrstvwxyz"
ans=""
s=input()
inp=s.lower()
for i in inp:
    if i not in ans:
        ans+=i
print(ans)        
        
