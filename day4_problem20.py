'''password verifier
mr.X is trying to create a new password for his instagram accout...
these are the required forcreating  new password
condition1: minimum length is 8 maximum length is 15
condition2:  only @,/ is allowed in a password
condition3:  no spaces are allowed 
condition4:  only alpha numerics are allowed
youe supposed to print weak if length is exact 8...medium length is between 8 to 12...
strong if length is between 12 to 15  '''
str=input()
var=len(str)
p="@"
q="/"
if var>=8 and var<=15:
    if p or q in str:
        if " " not in str:
            if var==8:
                print("weak") 
            elif var>8 and var<=12:
                print("medium")
            elif var>12 and var<=15:
                print("strong")
        else:
            print("check the condition")
    else:
        print("follow the conditions") 
else:
    print("please check the password") 



    
                      
    


         