all_age = [1,2,3,4,5,7,8]
for age in all_age:
    if age<=10:
        print(age)



def employee(basic,hr,mobile):
    new_salary = []

    all_salary = [{'basic':20000, 'hr':4000, 'mobile':2000},{'basic':18000, 'hr':3000, 'mobile':1000},
    {'basic':20000, 'hr':4000, 'mobile': 0},{'basic':15000, 'hr':4000, 'mobile':200}]

    
    for salary in all_salary:
            total=salary['basic'] + salary['hr'] + salary['mobile']
            new_salary.append(total)
            print(new_salary)
            c = (sum(new_salary))
            avg_total = c / len(new_salary)
            print(avg_total)


        # new_salary.append(all_salary)
        # zipped = (zip(new_salary))
        # print(zipped)
        # for z in zipped:
        #     all_salary
    

employee(20000,3000,100)




student_data = [{'id':1, 'Hacker' : 'DOSHI', 'Rank' : 43},
               {'id':2, 'Hacker' : 'JOSHI', 'Rank' : 45},
               {'id':3, 'Hacker' : 'MOSHI', 'Rank' : 41},
               {'id':4, 'Hacker' : 'LOSHI', 'Rank' : 98},
               {'id':5, 'Hacker' : 'AOSHI', 'Rank' : 14}]
counter = 0
sumRank = 0

for i in student_data:
    sumRank+=i['Rank']
    counter = counter+1

average = sumRank/counter
print(average)


class MyCar():
    def __init__(self,amount,quantity):
        self.amount = amount
        self.quantity = quantity

        total = self.quantity * self.amount
        print(total)

    def ok(self,amount,quantity):
        self.amount = amount
        self.quantity = quantity
        


class MyNewCar(MyCar):
    def new():
        pass


new = MyNewCar(100000,30000)
print(new.amount)
print(new.quantity)

c = MyCar(2000,300)
print(c.amount)
print(c.quantity)


class India():
    def capital(self):
        print("New Delhi is the capital of India.")
  
    def language(self):
        print("Hindi is the most widely spoken language of India.")
  
    def type(self):
        print("India is a developing country.")
  
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
  
    def language(self):
        print("English is the primary language of USA.")
  
    def type(self):
        print("USA is a developed country.")
  
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()


class A:
 
    def fun1(self):
        print('feature_1 of class A')
         
    def fun2(self):
        print('feature_2 of class A')
     
 
class B(A):
     
    # Modified function that is
    # already exist in class A
    def fun1(self):
        print('Modified feature_1 of class A by class B')   
         
    def fun3(self):
        print('feature_3 of class B')
         
 
# Create instance
obj = B()
     
# Call the override function
obj.fun1()


for i in range(1,100):
    if i%3==0:
        print('flip',i)
    elif i%5==0:
        print('flop',i)
    elif i%3==0 and i%5==0:

        print('flip flop',i)
    else:
        print('nothing',i)

bangla = int(input('enter your bangla marks : '))

english = int(input('enter your english marks :'))

total_marks = (bangla) + (english)

if total_marks > 100 or total_marks < 90:

    print("marks less than 90")

# elif total_marks == 100:
#     print("total marks 100")
else:
    print("others")

for age in range(1,100):
    print(age)



for number in range(1,101):
    if number % 4 == 0:
        print(number)

#Use of break statement inside the loop


for val in "string":
    if val == "i":
        continue
    print(val)

name = "mahin342545 tamjid"

slice_name = name[0:5]
print(slice_name)

a = "Hello"
c = "World"
d = a + c
print(d)

age = 36
txt = "My name is John, I am " + age
print(txt)



price = 100

mahih = "I want {} pieces of item {} for {} dollars."

print(mahih.format(price,price,price))


name = "mahin"
new_name = name.count("m")
c = name.capitalize()
d = name.upper()
print(d)
print(c)
print(new_name)



age_list = [10,23,12,13,34,34,23,23,13,1234,5,3,4,5,35]
for age in age_list:
    if age == 34:
        print(age)

import math


x = float(input('enter your x marks : '))

y = float(input('enter your y marks :'))

z = float(input('enter your y marks :'))


s = float((x + y + z)/2)

print(s)

sx = float(s-x)
sy = float(s-y)
sz = float(s-z)


sxyz = (math.sqrt((sx*sy*sz)))

Area = s*sxyz
print(Area)


sentence = input('enter your sentence : ')
l = []

for i in sentence:
    if i.isupper():

        if i not in l:
            l.append(i)
print(l)
# print(set(l))
string = " "
c = string.join(l)
print(c)


