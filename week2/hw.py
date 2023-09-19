#1 task
# result_str="";    
# for row in range(0,7):    
#     for column in range(0,7):     
#         if (((column == 1 or column == 5) and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5)):  
#             result_str=result_str+"*"    
#         else:      
#             result_str=result_str+" "    
#     result_str=result_str+"\n"    
# print(result_str);

#2 task
# result_str="";    
# for row in range(0,7):    
#     for column in range(0,7):     
#         if (column == 1 or ((row == 0 or row == 3) and column > 1 and column < 5) or (column == 5 and row != 0 and row < 3) or (column == row - 1 and row > 2)):  
#             result_str=result_str+"*"    
#         else:      
#             result_str=result_str+" "    
#     result_str=result_str+"\n"    
# print(result_str)

#3 task
# humanage = int(input())
# if humanage <=2:
#     dogage = humanage * 10.5
# else:
#     dogage = (humanage-2)*4 + 21
# print(dogage)

#4 task
# letter = input()
# if letter in ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'):
#     print(letter, "is a vowel")
# else:
#     print(letter, "is a consonant")

#5 task
# month = input()
# if month in ("January", "March", "May", "July", "August", "October", "December"):
#     print("No. of days: 31")
# elif month in ("April", "June", "September", "November"):
#     print("No. of days: 30")
# elif month == "February":
#     print("No. of days:28/29")


# 6 task
# a = int(input())
# b = int(input())
# c = a+b
# if (c>15 and c<20):
#     print("20")
# else:
#     print(c)

#7 task (not correct)
# string = input()
# if (type(string))==int:
#     print("The string is an integer.")
# else:
#     print("The string is not an integer.")

#8 task
# x = int(input())
# y = int(input())
# z = int(input())
# if (x==y and x==z and y==z):
#     print("Equilateral triangle")
# elif (x!=y and x!=z and y!=z):
#     print("Scalene triangle")
# elif (x==y or x==z or y==z):
#     print("Isosceles triangle")

#9 task
# month = int(input())
# day = int(input())
# if month==1:
#     print("January,", day,".Season is winter" )
# if month==2:
#     print("February,", day,".Season is winter" )
# if month==12:
#     print("December,", day,".Season is winter" )
# if month==3:
#     print("March,", day,".Season is spring" )
# if month==4:
#     print("April,", day,".Season is spring" )
# if month==5:
#     print("May,", day,".Season is spring" )
# if month==6:
#     print("June,", day,".Season is summer" )
# if month==7:
#     print("July,", day,".Season is summer" )
# if month==8:
#     print("August,", day,".Season is summer" )
# if month==9:
#     print("September,", day,".Season is autumn" )
# if month==10:
#     print("October,", day,".Season is autumn" )
# if month==11:
#     print("November,", day,".Season is autumn" )

#10 task
# day = int(input("Day of birthday:"))
# month = input("Name of month:")
# if month == 'december':
# 	astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
# elif month == 'january':
# 	astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
# elif month == 'february':
# 	astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
# elif month == 'march':
# 	astro_sign = 'Pisces' if (day < 21) else 'Aries'
# elif month == 'april':
# 	astro_sign = 'Aries' if (day < 20) else 'Taurus'
# elif month == 'may':
# 	astro_sign = 'Taurus' if (day < 21) else 'Gemini'
# elif month == 'june':
# 	astro_sign = 'Gemini' if (day < 21) else 'Cancer'
# elif month == 'july':
# 	astro_sign = 'Cancer' if (day < 23) else 'Leo'
# elif month == 'august':
# 	astro_sign = 'Leo' if (day < 23) else 'Virgo'
# elif month == 'september':
# 	astro_sign = 'Virgo' if (day < 23) else 'Libra'
# elif month == 'october':
# 	astro_sign = 'Libra' if (day < 23) else 'Scorpio'
# elif month == 'november':
# 	astro_sign = 'scorpio' if (day < 22) else 'Sagittarius'
# print("Your Astrological sign is :",astro_sign)

#11 task
# year = int(input())
# if year  % 12 == 0:
#     sign = 'Dragon'
# elif year % 12 == 1:
#     sign = 'Snake'
# elif year % 12 == 2:
#     sign = 'Horse'
# elif year % 12 == 3:
#     sign = 'sheep'
# elif year % 12 == 4:
#     sign = 'Monkey'
# elif year % 12 == 5:
#     sign = 'Rooster'
# elif year % 12 == 6:
#     sign = 'Dog'
# elif year % 12 == 7:
#     sign = 'Pig'
# elif year % 12 == 8:
#     sign = 'Rat'
# elif year % 12 == 9:
#     sign = 'Ox'
# elif year % 12 == 10:
#     sign = 'Tiger'
# else:
#     sign = 'Hare'

# print("Your Zodiac sign :",sign)

#12 task
# x = int(input())
# y = int(input())
# z = int(input())
# if ((x<y and x>z) or (x<z and x>y)) :
#     print("The median is:", x)
# elif (y<x and y>z) or (y<z and y>x):
#     print("The median is:", y)
# elif (z<x and z>y) or (z<y and z>x):
#     print("The median is:", z)

#14 task
# print("Input some integers to calculate their sum and average. Input 0 to exit.")

# count = 0
# sum = 0.0
# number = 1

# while number != 0:
# 	number = int(input(""))
# 	sum = sum + number
# 	count += 1

# if count == 0:
# 	print("Input some numbers")
# else:
# 	print("Average and Sum of the above numbers are: ", sum / (count-1), sum)

#15 task
# n = int(input())

# for i in range(1,11):
#    print(n,'x',i,'=',n*i)