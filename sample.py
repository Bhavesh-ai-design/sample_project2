#Experiment !. Complete Python Program 
import pandas as pd 
import matplotlib.pyplot as plt 
# Create employee dataset 
employee_data = { 
    "EmpName": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"], 
    "EmpId": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
    "Gender": [ 
        "Male", "Male", "Male", "Female", "Female", 
        "Female", "Male", "Female", "Male", "Male" 
    ], 
    "Age": [30, 32, 35, 45, 23, 21, 24, 35, 22, 28], 
    "Income": [ 
        15000, 13000, 16000, 25000, 13000, 
        12000, 15000, 30000, 14000, 29000 
    ], 
    "MaritalStatus": [ 
        "Unmarried", "Married", "Married", "Married", 
        "Unmarried", "Unmarried", "Unmarried", 
        "Married", "Unmarried", "Divorced" 
    ] 
} 
 
df = pd.DataFrame(employee_data) 
 
# Display data 
print("EMPLOYEE DATASET") 
print(df.to_string(index=False)) 
 
# Descriptive statistics 
print("\nDESCRIPTIVE STATISTICS") 
print(df[["Age", "Income"]].describe()) 
# Central tendency 
print("\nCENTRAL TENDENCY") 
print("Mean Age:", round(df["Age"].mean(), 2)) 
print("Median Age:", df["Age"].median()) 
print("Mode Age:", df["Age"].mode().tolist()) 
print("Mean Income:", round(df["Income"].mean(), 2)) 
print("Median Income:", df["Income"].median()) 
print("Mode Income:", df["Income"].mode().tolist()) 
# Dispersion 
for variable in ["Age", "Income"]: 
    data_range = df[variable].max() - df[variable].min() 
variance = df[variable].var() 
standard_deviation = df[variable].std() 
iqr = ( 
df[variable].quantile(0.75) - 
df[variable].quantile(0.25) 
) 
cv = (standard_deviation / df[variable].mean()) * 100 
print(f"\nDISPERSION OF {variable.upper()}") 
print("Range:", data_range) 
print("Variance:", round(variance, 2)) 
print("Standard Deviation:", round(standard_deviation, 2)) 
print("Interquartile Range:", round(iqr, 2)) 
print("Coefficient of Variation:", round(cv, 2), "%") 
# Categorical distributions 
print("\nGENDER DISTRIBUTION") 
print(df["Gender"].value_counts()) 
print((df["Gender"].value_counts(normalize=True) * 100).round(2)) 
print("\nMARITAL STATUS DISTRIBUTION") 
print(df["MaritalStatus"].value_counts()) 
print( 
(df["MaritalStatus"].value_counts(normalize=True) * 100).round(2) 
) 
# Group-wise summary 
print("\nGENDER-WISE STATISTICS") 
print( 
df.groupby("Gender")[["Age", "Income"]] 
.agg(["count", "mean", "min", "max", "std"]) 
.round(2) 
) 
# Visualisations 
df["Gender"].value_counts().plot( 
kind="bar", 
color=["steelblue", "lightcoral"], 
edgecolor="black" 
) 
plt.title("Gender Distribution") 
plt.xlabel("Gender") 
plt.ylabel("Frequency") 
plt.xticks(rotation=0) 
plt.tight_layout() 
plt.show() 
df["MaritalStatus"].value_counts().plot( 
kind="pie", 
autopct="%1.1f%%", 
startangle=90 
) 
plt.title("Marital Status Distribution") 
plt.ylabel("") 
plt.tight_layout() 
plt.show() 
plt.hist(df["Age"], bins=5, color="green", edgecolor="black") 
plt.title("Age Distribution") 
plt.xlabel("Age") 
plt.ylabel("Frequency") 
plt.tight_layout() 
plt.show() 
plt.hist(df["Income"], bins=5, color="purple", edgecolor="black") 
plt.title("Income Distribution") 
plt.xlabel("Income") 
plt.ylabel("Frequency") 
plt.tight_layout() 
plt.show()