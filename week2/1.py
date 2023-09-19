#1 task
# thislist = []
# for n in range (1500, 2700):
#     if (n%5==0) and (n%7==0):
#         thislist.append((n))
# print(thislist)

#2 task
# print ("Write the temperature in Celcius: ")
# c = float(input())
# print ("Write the temperature in Fahrenheit: ")
# f = float(input())
# fc = 5/9*(f-32)
# cf = (c*9/5) + 32
# print(c,"°C is", cf, "in Fahrenheit")
# print(f,"°F is", fc, "in Celsius")

#3 task
# import random
# n2, n1=random.randint(1,10),0
# while n2 != n1:
#     n1=int(input())
# print("True")

#4 task


#5 task
# txt = str(input())[::-1]
# print(txt)

#6 task
even=0
odd=0
mylist = []
n = int(input())
for num in range(n):
    x = int(input())
    mylist.append(x)
    if x%2==0:
      even=even+1
    else:
      odd=odd+1
print("Number of odd numbers:", odd)
print("Number of even numbers:", even)

#7 task
