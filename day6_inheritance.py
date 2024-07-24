'''implementing single inheritance'''

# class Animal:
#     def speak():
#         return "animal is speaking"
# 
# class Dog(Animal):
#     def bark():
#         return "bow...." 
# obj1=Animal

# obj2=Dog
# print(obj1.speak())
# print(obj2.bark())

'''implementing multilevel inheritance'''

class Animal:
    def speak():
        return "animal is speaking"

class Dog(Animal):
    def bark():
        return "bow...." 
class puppy(Dog):
    def puppy_speak():
        return "im puppy"  
obj1=Animal
obj2=Dog
obj3=puppy
#print(obj1.speak())
#print(obj2.bark())
print(obj3.puppy_speak())

'''multiple inharitance'''
# class father:
#     def father_speak():
#         return "father class"
# class mother:
#     def mother_speak():
#         return "mother class"  
# class kid(father,mother):
#     def kid_speak():
#         return "im kid... im having properties og both"   
# obj1=kid
# print(obj1.father_speak())  
# print(obj1.mother_speak())
# print(obj1.kid_speak())

