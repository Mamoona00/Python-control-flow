#Loops in python
#for loop
x = "Mamoona"
for n in x:
    print(n)

for i in range(0, 10, 2):         #range in for
    print("Number: " , i)

#else with for
x = 8 , 16 , 24, 32 , 40
for i in x:
    print(i)
else:
    print("out of the loop") 

#while loop
n = 5
while n <= 12:
    print(n)
    n = n + 1  #increament         

i = 7
while i > 2:
    print(i)
    i = i - 1    #decreament

i = 0
while i <= 3:       #else with while
    print(i)
    i += 1
else:
    print("Loop terminated")

   
#control statements
#coninue
Students = "Ali" , "Ahmad" , "Hoor" , "Noor"
for name in Students:
    if (name =="Ahmad"):
        continue
    print(name)


#break
num = 1
while num < 5:
    if num == 3:
        break
    print(num)
    num = num + 1
marks = 10 , 20 , 30 , 40 , 50
for i in marks:
    if (i == 40):
        break
    print(i)
#pass
a = "Mamoona Shamraiz"
for S in a:
    pass
print(S)

#looping techniques in python
#sorted()
n = [2, 5, 10, 2 , 50 , 35, 65, 89,50]
print("The numbers in sorted order: ")
for i in sorted(n):
    print(i)
#set()
print("The numbers in sorted order without duplicating: ")
for i in sorted(set(n)):
    print(i)
#reversed()
print("List after reversing elements: ")
for i in reversed(n):
    print(i)
#inumerate()
x = ["X", "Y" , "Z"]
for i in enumerate(x):
    print(i)

for key,value in enumerate(x):
    print(key,value)      #output is not in tuple
#zip()
x = ["cs504" , "cs403", "cs304"]
y = ["Mak Book" , "Fisal kaleem" , "KST learning"]
z = [1 , 2 , 3]
for n in zip(x,y,z):
    print(n)
#items() 
dict = {'Physics': 'P' , 'Chemistry': 'C' , 'Computer Science': 'CS'}
print("output using items: ")
for key , value in dict.items():
    print(key , value)

#range()
print("Items in range are:")
for x in range(1, 10):
    print(x)
#pyramid program
num = 5
for m in range(0 , num):
    for n in range(0 , num - m - 1):
        print(end = " ")
    for n in range(0 , m + 1):
        print("*" , end = " ")
    print()

rows = 5
for i in range(0, rows + 1):
  for j in range(i):
    print("*", end=" ")
  print()


num = 5
for m in range(num , 0 , -1):
    for n in range(m):
        print("*" , end = " ")
    print()

#Chaining comparison operators
a = 23
print(10 < a < 50)
x = 45
y = 23
print(x>y and x<y)  

#Switch function
number = 30
if number == 20:
    print("Number is equal to twenty.")
elif number < 20:
    print("Number is less than twenty")
elif number > 20:
    print("Number is greater than twenty")
else:
    print("Number is not equal to twenty")

Noodles = {
    1 : 'Blazin',
    2 : 'Chatpata',
    3 : 'Chicken',
    4 : 'Spciy tikka'
}
def flavoures(num):
   return Noodles.get(num)
fav = flavoures (1)
print("My fav flavour is :" , fav)

#count()
import itertools
c = itertools.count(1, 3)
for n in c:
    print(n)
    if n == 10:
        break
    
#repeat()
a = "Mamoona"
for i in itertools.repeat(a , 4):
    print(i)

#chain()
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
n = itertools.chain(l1 , l2)
print(list(n))

#iter() and next()
#iterator
list = [7 , 14 , 21 , 28 , 35]
x = iter(list)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
#generators
def gen(n):
    for x in range(n):
        yield x
for i in gen(5):
    print(i)

#generator expression
sps = (x for x in range(7))
for i in sps:
    print(i)

