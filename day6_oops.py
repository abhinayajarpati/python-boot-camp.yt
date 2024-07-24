'''OOPS(OBEJECT ORIENTED PROGRAMMING LANGUAGE)

CLASS:::>>>blue print of an object
OBJECT--->>> instance of class
properties of an object can be unique and common''' 

  
#creating a class
# class Myclass():
#     def add(a,b):
#         return(a+b)
#     def sub(a,b):
#         return(a-b)
#     def mul(a,b):
#         return(a*b)
#     def div(a,b):
#         return(a/b)
#     def mod(a,b):
#         return(a%b)
# obj1=Myclass
# obj2=Myclass           #creating object
# print(obj1.add(2,5))
# print(obj2.add(5,6))
# print(obj1.sub(2,5))
# print(obj2.sub(5,6))
# print(obj1.mul(2,5))
# print(obj2.mul(5,6))
# print(obj1.div(2,5))
# print(obj2.div(5,6))
# print(obj1.mod(2,5))
# print(obj2.mod(5,6))


'''CONSTRUCTOR AND DISTRUCTOR
CONSTRUCTOR--->>> program execution starts from constructor

 CREATING A CONSTRUCTOR'''
class Myclass():
    def __init__(self.a,b):
        self.a=a
        self.b=b
        return "im constructor"
obj1=Myclass
print(obj1.add(5,7))


'''CLASS VARIABLE AND INSTANCE VARIABLE'''
# class Myclass:
#     cls_var="im class variable"
#     def sub(a,b):
#         ins_var_sub="im instance variable"
#         print(ins_var_sub)
#         return(a-b)
# obj1=Myclass
# print(obj1.sub(5,3))


''' PLIILARS OF OOPS'''
'''1)ABSTRACTION--->>>'''#it will hide the unnccessary information AND shows the top level information
#IT WILL achivied with access specifiers

'''ACCESS SPECIFIERS--->>'''#which specifies the access
'''TYPES---->'''#PUBLEC(evryone can access)
                #PRIVATE(only yuorslef)
                #PROTECTED(limited access)

'''2)POLIMORPHISM'''#different propertices/one method performs different behaviour in differnt situations
#runtime polimorphism
#compiletime polimorphism

'''3)ENCAPSULATION'''#all the files are bundled and stored in capsule format/single file

'''4)INHERITANCE'''#need of this is reusability  
#types___>>#single
           #multiple
           #multilevel
           #heirachical

   