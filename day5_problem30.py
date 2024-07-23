'''remove all the brackets from the given algebric expresion'''



# s=input()
# r=['(',')','{','}','[',']']
# for i in s:
#     if i not in r:
#         print(i,end="")
        
                                          #{==123  }==125
                                             #)==41 (==40  [==91  ]==93
        
n=input() 
for i in n:
    if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
        pass
    else:
        print(i,end="") 
print()     
