#1
x="love python"

for i in range(5):
    print(x)

#2
ls=[]

for i in range(1,11):
    ls.append(i)

print(ls)

#3

x=[10,1,9,2,8,3,7,4,6,5]

for i in range(len(x))
    print(i)

y=sorted(x)
print(y)


#4

x=[]

count_big_10=0
count_small_10=0
max=0
count_even=0
count_divded_3=0
#א
for i in range(11):
    num=int(input("enter number"))
    x.append(num)
print(sum(x))

#ב
for j in x:
    print(j/11)

for a in x:
    if a>10:
        count_big_10+=1
    if a<10:
        count_small_10+=1
    if a>max:
        max=a
    if a%2== 0:
        print(a)
    if a%3==0:
        count_divded_3+=1

print(count_big_10)
print(count_small_10)
print(max)
print(a,end=' ')
print(count_divded_3)


#5
data=[1,2,2,9,7,7]

for i in range(len(data)):
    if data[i]==data[i-1]:
        print(data[i])

#א
data.insert(0,3)

print(data)

#ב
x=int(input("enter number"))

data.insert(1,x)
print(data)

#ג
a=data[0]+data[1]

data.insert(2,a)
print(data)

#ד
b=data[0]*data[1]*data[2]

data.insert(3,b)
print(data)

#ה
print(data)


#6
x=[]
y=[]

for i in range(5):
    grade_x=int(input("tamir enter your grade"))
    x.append(grade_x)
    grade_y=int(input("ofir enter your grade"))
    y.append(grade_y)

for i in x:
    for j in y:
        if i==j:
            print("same grades",i)

#7
name=input("enter your name")
print(len(name))
if len(name)%2==0:
    print("The length of the string is even")

#8

shvil=[]

sum=0
for i in range(3):
    road=input("name of the road")
    distance=int(input("enter Length of section"))
    shvil.append([road,distance])
    sum += distance
    if distance > 10:
        print(distance)


print("bigger then 10km:",road)
print("the length of shvil:",sum)

#9
order=[]
price_for_box=35
fee=10
sum=0
count_bigger_20=0
for i in range(2):
    name=input("customer name")
    box=int(input("how many box?"))
    order.append([name,box])
    sum+=box
    if box<4:
        print("you need to pay 10 nis for delivery fee,total:",sum*price_for_box+fee)
    if box>20:
        count_bigger_20+=1
        print(name,"total price:",sum*price_for_box)
    print("bigger20:",count_bigger_20)
print(order)

#10

family=[]
sum_kids=0
for i in range(2):
    name=input("enter last name")
    family.append(name)
    kids=int(input("how many kids go to trip?"))
    sum_kids+=kids
    if kids>3:
        print("you have discount")

print(sum_kids,"children going on a trip")

