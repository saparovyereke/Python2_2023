import matplotlib.pyplot as plt

sizes = [17.7, 10.7, 10.2, 10.2, 21, 30.3]
labels = ['A', 'B', 'C', 'D', 'E', 'F']

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

plt.axis('equal')

plt.show()

sizes2 = [3.6, 3.8, 4.1, 4.2, 5.3]
labels2 = ['Under 35', '35-49', '50-65', 'Over 65']
bottom = 1
width = .2

