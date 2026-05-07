Aim:
a. Write a Program to Load, Clean and Exploring the data using python. 

Algorithm:
Data Loading
Step1: Start
Step2: Import required libraries (pandas, numpy) 
Step3: Load dataset using read_csv() 
Step4: Store dataset in a variable (e.g., data) 
Data Cleaning 
Step5: Check for missing values using isnull() 
Step6: If missing values exist:
Step7: Replace with mean/median OR 
Step8: Remove rows/columns 
Step9: Check for duplicate records using duplicated() 
Step10: Remove duplicates using drop_duplicates() 
Step11: Check data types using dtypes 
Step12: Convert data types if required Step 3: Data Exploration (EDA) 
Step13: Display first few records using head() 
Step14: Display last few records using tail() 
Step15: Get dataset structure using info() 
Step16: Generate statistical summary using describe() 
Step17: Find correlation between variables using corr()
Step18: Display cleaned and analyzed data 
Step19: Stop

b. Write a Program to implement various types of visualization in python.
ALGORITHM:
Step 1: Import Libraries
Import matplotlib.pyplot and pandas
Step 2: Load Data
Read dataset using read_csv()
Step 3: Create Visualizations
Line Chart → Trend over time
Bar Chart → Category comparison
Histogram → Data distribution
Pie Chart → Percentage distribution
Scatter Plot → Relationship between variables
Step 4: Display Graphs
Use plt.show() for each graph

Source code:
#Program to Load, Clean and Explore Data in Python
# Import libraries
import pandas as pd
import numpy as np

# Load dataset
data = pd.read_csv("data.csv")

# Display first 5 rows
print("First 5 rows:")
print(data.head())

# Check dataset info
print("\nDataset Info:")
print(data.info())

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Fill missing values with mean (for numeric columns)
data.fillna(data.mean(numeric_only=True), inplace=True)

# Remove duplicate rows
data.drop_duplicates(inplace=True)

# Explore data
print("\nStatistical Summary:")
print(data.describe())

# Column names
print("\nColumns:")
print(data.columns)

# Value counts of a column (example)
# Replace 'column_name' with actual column
# print(data['column_name'].value_counts())

#Program for Various Types of Visualization in Python
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("data.csv")

# -------- Line Plot --------
plt.plot(data['column1'], data['column2'])
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# -------- Bar Chart --------
data['column1'].value_counts().plot(kind='bar')
plt.title("Bar Chart")
plt.show()

# -------- Histogram --------
plt.hist(data['column1'], bins=10)
plt.title("Histogram")
plt.show()

# -------- Scatter Plot --------
plt.scatter(data['column1'], data['column2'])
plt.title("Scatter Plot")
plt.show()

# -------- Pie Chart --------
data['column1'].value_counts().plot(kind='pie')
plt.title("Pie Chart")
plt.show()

# -------- Seaborn Plot (Boxplot) --------
sns.boxplot(x=data['column1'])
plt.title("Box Plot")
plt.show()
  
Output:
a.
---- Original Data ----
   Age  Salary
0   25   50000
1   30   60000
2   NaN  55000

Missing Values:
Age       1
Salary    0

---- Cleaned Data ----
   Age  Salary
0  25.0  50000
1  30.0  60000
2  27.5  55000

First 5 Rows:
   Age  Salary
0  25.0  50000
1  30.0  60000
2  27.5  55000

Statistical Summary:
           Age      Salary
count   3.0000    3.000000
mean   27.5000  55000.000000

b.
Sample Output (Explanation)
Line Plot → Shows trend of salary vs age
Bar Chart → Compares salary across ages
Histogram → Shows salary distribution
Pie Chart → Percentage share of salaries
Scatter Plot → Relationship between age & salary
