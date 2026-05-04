Experiment 9(a): NumPy and Pandas

AIM:
To write a Python program to implement NumPy and Pandas packages.

ALGORITHM:
Step1: Import NumPy and Pandas libraries.  
Step2: Create a NumPy array.  
Step3: Perform basic operations like mean and sum.  
Step4: Create a dictionary with sample data.  
Step5: Convert the dictionary into a Pandas DataFrame.  
Step6: Display the DataFrame.  
Step7: Calculate average of a column.  

Experiment 9(b): Matplotlib and Pandas

AIM:
To write a Python program to implement Matplotlib and Pandas libraries.

ALGORITHM:
Step1: Import Pandas and Matplotlib libraries.  
Step2: Create a dataset using a dictionary.  
Step3: Convert it into a DataFrame.  
Step4: Display the DataFrame.  
Step5: Plot a bar chart using Matplotlib.  
Step6: Add title and labels.  
Step7: Display the graph.  

Source code:
# Import libraries
import numpy as np
import pandas as pd

# --------- NumPy Example ---------
print("NumPy Example:")

# Create a NumPy array
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

# Perform operations
print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))


# --------- Pandas Example ---------
print("\nPandas Example:")

# Create a dictionary
data = {
    "Name": ["A", "B", "C"],
    "Marks": [85, 90, 78]
}

# Convert to DataFrame
df = pd.DataFrame(data)

print("DataFrame:")
print(df)

# Display basic info
print("Average Marks:", df["Marks"].mean())

Output:
NumPy Example:
Array: [10 20 30 40 50]
Mean: 30.0
Sum: 150

Pandas Example:
DataFrame:
  Name  Marks
0    A     85
1    B     90
2    C     78
Average Marks: 84.33333333333333
  Name  Marks
0    A     70
1    B     85
2    C     90
3    D     60
