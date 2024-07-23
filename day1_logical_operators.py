''''1)and,
or'''
# age=int(input())
# if (age>18 and age<24):
#     print("allow to drive the two wheeler")
# elif (age>=24 and age<45):
#     print("two and four wheelers")
# else:
#     print("all")
'''2)person x goes to market he will buy 10 apples and two dozon bananas and he will buy 8 oranges 
next the cost of ech apple is 15 rupees and cost of oranges 5 rupees and cost of banana is 4 rupees
and mother of x i.e Y gave 700 rupees to mr.x and says some amount will be left with you'''
# cost_apples=15
# cost_bananas=4
# cost_oranges=5

# apples=int(input())
# bananas=int(input())
# oranges=int(input())

# total=0
# total=cost_apples*apples+cost_bananas*bananas+cost_oranges*oranges
# print(total)
# if total<700:
#     print("shopkeeper is not a cheater")
# else:
#     print("he is cheater")

'''3)take input from user if it is positive and even print positive even or ..... '''
# num=int(input())
# if (num>0 and num%2==0):
#     print("postive evne number")
# elif(num<0 and num%2==0):
#     print("negative even number")
# elif(num>0 and num%2!=0):
#     print("positive odd number")
# else:
#     print("negative odd number")

'''4)mr.Z is selected for olympics he is perticipating swimming compition only 1 member 
 is selected among 100 of participants anyhow 
 he got selected... mr.x and mr.y are the friends of z mr.x is
 participating badminton and mr.y participating to the tennis.....
 according to the selection comitte the requirements
 for the badminton players are 140cm height and weight is factors of 2. bodyfat 
 is lessthan 12%.....according to the selection comitte requirements
 for the table tennis are height minimum 118cm to 148cm
 weight is factors of number of medals got by mr.z ,bodyfat 14%.... 
 according to the previous history z participated in 14 games out of 
 which having success rate of 50% 
 write a program whether mr.x and mr.y and mr.z from india will 
 travel in same plane or write wthether that 3 persons will meet inmeet olympic '''

height_x=int(input())
height_y=int(input())
weight_x=int(input())
weight_y=int(input())
x_selected=0
y_selecetd=0
if(height_x==140 and weight_x%2==0):
    x_selected+=1
    #print(x_selected)
if((height_y<148 and height_y>118) and weight_y%7==0):
    y_selected+=1
    #print(y_selected)
if(y_selecetd==1 and x_selecetd==1):
    print("x,y and z will meet in aeroplane")
else:
    print("they not meet")






