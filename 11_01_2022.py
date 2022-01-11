#variable declaration

bangla=20
english=30
total=(bangla+english)
avg=(total/2)
print(total)

#number
abid=200
tamjid=2.15
ifty=-5j
print(type(abid))
print(type(tamjid))
print(type(ifty))

#confitional logic
age=int(input('Enter your age:'))
if age>50:
    print('old')
elif age>20 and age<50:
    print('adult')
else:
    print('children')


a = 10
print(a)
print(type(a))
c = (str(a))
print(c)
print(type(c))

d = int(c)
print(d)
print(type(d))


department = "Eng"
roll = 101
student_id = department + '-' + str(roll)

print(student_id)

number=200
for s in range(1,200):
    if s%20==0:
        print(s)
        break


