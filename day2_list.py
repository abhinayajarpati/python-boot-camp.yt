'''declaration of a LIST'''
# my_list=[1,2,3,4]
# print(*my_list)
# my_list.append(44)
# print(*my_list)
# my_list.insert(3,55)
# print(*my_list)
# my_list.pop(2)      #pop itself delete the last number of the list but we take index number, mentioned 
#                     #index element will deleted
# print(*my_list)
# '''adding of 2 LISTS'''
# my_list1=[1,2,-13,41,545,-6,7]
# print(len(my_list1))
# my_list2=[5,6,7,8]
# new_list=my_list1+my_list2
# new_list=my_list1.copy()
# cnt=my_list1.count(2)
# print(cnt)
# my_list1.sort()    #in the background the list was sorted i.e quick sort i.e time complexity 
#                        #is nlogn but we want n time complexit
# print(*my_list1) #ascending order

'''aggrigate functions'''
#print(sum(my_list1))

'''taking dynamic input in a LIST'''
#my_list=list(map(int,input().split(",")))
    #map=to print many elements  split=default space
#print(*my_list)
# my_list2=list(map(str,input().split(",")))
# print(*my_list2)
# print(my_list2.count(2))
#my_list2.append(77)
'''take list from the user if user enters 1 append
enters 2 pop 3 enetrs sort 4=cancatination'''
list1=list(map(int,input().split()))
print("select any choices:1.append 2.pop 3.sort 4.cancatination")
choice=int(input())
if choice==1:
    list1.append(2)
    print(list1)
elif choice==2:
    list1.pop(2)
    print(list1)
elif choice==3:
    list1.sort()
    print(list1)
else:
    print(f"hello good morning length of the list is {len(list1)}")





           