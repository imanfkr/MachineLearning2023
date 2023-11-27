# -*- coding: utf-8 -*-
"""HW2_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wAM9cSc7IEE19BcwJgZO-1s576TdFCoa
"""

# QUESTION(1)

import numpy as np

random_integers = np.random.randint(1, 101, 20) # Create a NumPy array of 20 random integers between 1 and 100

# mean
mean = np.mean(random_integers)

# median
median = np.median(random_integers)

# standard deviation
std_dev = np.std(random_integers)

print("Random Integers:", random_integers)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)

# QUESTION(2)

import pandas as pd

data = {
    'Name': ['Ali', 'Iman', 'Ramin', 'Mohammad', 'Reza'],
    'Age': [20, 22, 25, 30, 50],
    'City': ['Tehran', 'Amol', 'Yazd', 'Hamedan', 'Sari']
}

df = pd.DataFrame(data)

# the first 3 rows
print(df.head(3))

# the last 2 rows
print("\n")
print(df.tail(2))

# summary
print("\n")
print(df['Age'].describe())

# QUESTION(3)

import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May"]
sales = [50000, 55000, 70000, 49000, 85000]

plt.bar(months, sales, color='red')
plt.xlabel("$Month$")
plt.ylabel("$Sales Amount$")
plt.title("$Monthly Sales for the Store (January to May)$")
plt.grid(axis='y', linestyle='--')

# Display the chart
plt.show()

# QUESTION(4)

import numpy as np

arr1 = np.random.randint(1, 10, (5, 5))
arr2 = np.random.randint(1, 10, (5, 5))

addition = arr1 + arr2
subtraction = arr1 - arr2
multiplication = arr1 * arr2
division = arr1 / arr2

print("arr1:\n", arr1)
print("arr2:\n", arr2)
print("Addition:\n", addition)
print("subtraction:\n", subtraction)
print("multiplication:\n", multiplication)
print("Division:\n", division)

# QUESTION(5)

import pandas as pd

# Sample DataFrame (replace this with your actual DataFrame)
data = {
    'Name': ['Ali', 'Iman', 'Reza', 'Amir'],
    'Age': [28, 32, 20, 35]
}

df = pd.DataFrame(data)

# Filter and display employees older than 30
filtered_df = df[df['Age'] > 30]

print(filtered_df)

# QUESTION(6)

import matplotlib.pyplot as plt
import numpy as np


x = np.random.rand(100)
y = np.random.rand(100)

plt.scatter(x, y, c='b', marker='o', label='Random Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.title('Scatter Plot of Random Data')

plt.legend()
plt.grid(True, linestyle='--')
plt.show()

# QUESTION(7)

import numpy as np

matrix1 = np.random.rand(2, 3)
matrix2 = np.random.rand(3, 4)

r = np.dot(matrix1, matrix2)

print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)
print(" Multiplication Result:\n", r)

# QUESTION(8)

import pandas as pd

data = {
    'Product Category': ['Jewellery', 'Clothing', 'Books', 'car','Books','Jewellery','car'],
    'Sales Amount': [700, 500, 300, 1000, 500, 800, 2000]
}

sales_df = pd.DataFrame(data)
category_sales = sales_df.groupby('Product Category')['Sales Amount'].sum().reset_index()
category_sales.rename(columns={'Sales Amount': 'Total Sales'}, inplace=True)
print(category_sales)

# QUESTION(9)

import matplotlib.pyplot as plt

years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
population = [20000, 23000, 25000, 28000, 29000, 32000, 34000, 37000, 39000, 40000]

plt.plot(years, population, marker='o', c='r' , linestyle='-')
plt.xlabel('$Year$')
plt.ylabel('$Population$')
plt.title('$City Population Growth Over 10 Years$')
plt.grid(True, linestyle='--')
plt.show()

# QUESTION(10)

import pandas as pd
import numpy as np

data = {
    'Name': ['Ali', 'Iman', 'Reza', 'Parsa'],
    'Score': [88, 99, 74, 67]
}

students_df = pd.DataFrame(data)

g= [
    students_df['Score'] >= 90,
    (students_df['Score'] >= 80) & (students_df['Score'] < 90),
    (students_df['Score'] >= 70) & (students_df['Score'] < 80),
    students_df['Score'] < 70
]

grades = ['A', 'B', 'C', 'D']

students_df['Grade'] = np.select(g, grades, default='F')
print(students_df)

# QUESTION(11)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Month': pd.date_range(start='2021-01-01', periods=24, freq='M'),
    'Product A Sales': [500, 480, 600, 750, 900, 850, 920, 1100, 1300, 1350, 1500, 1450, 1550, 1600, 1650, 1600, 1500, 1400, 1600, 1700, 1800, 1750, 1850, 1900],
    'Product B Sales': [300, 320, 400, 450, 500, 580, 700, 750, 820, 900, 950, 980, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1500, 1600, 1550, 1700],
    'Product C Sales': [200, 210, 250, 280, 320, 350, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720]
}

sales_df = pd.DataFrame(data)

# Task 1:

total_sales = sales_df[['Product A Sales', 'Product B Sales', 'Product C Sales']].sum()
print("Total Sales for Each Product:")
print(total_sales)

# Task 2:

average_sales = sales_df[['Product A Sales', 'Product B Sales', 'Product C Sales']].mean()
print("\nAverage Monthly Sales for Each Product:")
print(average_sales)

# Task 3:

max_sales_month_A = sales_df.loc[sales_df['Product A Sales'].idxmax()]
max_sales_month_B = sales_df.loc[sales_df['Product B Sales'].idxmax()]
max_sales_month_C = sales_df.loc[sales_df['Product C Sales'].idxmax()]
print("\nMonth with Highest Sales for Product A:")
print(max_sales_month_A)
print("\nMonth with Highest Sales for Product B:")
print(max_sales_month_B)
print("\nMonth with Highest Sales for Product C:")
print(max_sales_month_C)

# Task 4:

sales_2021 = sales_df.loc[0:11][['Product A Sales', 'Product B Sales', 'Product C Sales']].sum()
sales_2022 = sales_df.loc[12:23][['Product A Sales', 'Product B Sales', 'Product C Sales']].sum()
percentage_change = ((sales_2022 - sales_2021) / sales_2021) * 100
print("\nPercentage Change in Sales from January to December in 2022:")
print(percentage_change)

# Task 5:

plt.plot(sales_df['Month'], sales_df['Product A Sales'], label='Product A')
plt.plot(sales_df['Month'], sales_df['Product B Sales'], label='Product B')
plt.plot(sales_df['Month'], sales_df['Product C Sales'], label='Product C')
plt.xlabel('$Month$')
plt.ylabel('$Sales Amount$')
plt.title('$Monthly Sales Data for Each Product (2021-2022)$')
plt.legend()
plt.grid(True, linestyle='--')
plt.show()

# Task 6:

correlation = sales_df[['Product A Sales', 'Product B Sales']].corr().iloc[0, 1]
print("\nCorrelation between Product A and Product B Sales:")
print(f"Correlation coefficient: {correlation:.2f}")