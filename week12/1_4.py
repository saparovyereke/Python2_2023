import matplotlib.pyplot as plt

countries = ['Germany','India', 'UK', 'US', 'South Korea', 'Australia']
size = [16.5, 27.8, 24.6, 18.5, 9.2, 3.4]
Explode = [0, 0, 0, 0.2, 0, 0]
colours = ['cyan', 'red', 'green', 'blue', 'yellow', 'purple']
plt.pie(size, explode = Explode, autopct='%1.2f%%', labels = countries, shadow = True, startangle = 45, colors = colours)
plt.title('Population Density Index')
plt.axis('equal')
plt.show()