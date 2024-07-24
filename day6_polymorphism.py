'''POLYMORPHISM'''
'''METHOD OVERRIDING'''
# class animal:
#     def speak():
#         return "speaking...."
# class dog(animal):
#     def speak():
#         return "dog is speaking..."  
# class puppy(dog):
#     def speak():
#         return "puppy is speaking....."  
# obj1=animal
# obj2=dog
# obj3=puppy
# print(obj1.speak())    
# print(obj2.speak())   
# print(obj3.speak()) 

'''METHOD OVERLOADING'''
class cal:
    def add(self,*args):             #"SELF"-->used to assign variables
        sum=0
        for i in args:
            sum+=i

        return (sum)
obj1=cal()                       #for dynamic input put '#'
print(obj1.add(1,2))
print(obj1.add(1,2,3))
print(obj1.add(1,2,3,4))
    

