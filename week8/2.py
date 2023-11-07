# class Investment():
#     def __init__(self, p, summa):
#         self. p = p
#         self.summa = summa
        
#     def value_after(n):
#         return self. p*(1+self.summa/100)**n
    
#     def __str__():
#         return f'Principal is {self.p}, Summa vklada is {self.summa}'

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

print(mydb)