import pandas as pd

# Load the CSV file
df = pd.read_csv("salaries_by_college_major.csv")

# Drop any rows with missing values (e.g., the last row with "Source: PayScale Inc.")
df = df.dropna()

# Convert salary columns to numeric (in case they are read as strings)
salary_columns = [
    "Starting Median Salary",
    "Mid-Career Median Salary",
    "Mid-Career 10th Percentile Salary",
    "Mid-Career 90th Percentile Salary"
]
df[salary_columns] = df[salary_columns].apply(pd.to_numeric)

# Calculate average salaries
average_salaries = df[salary_columns].mean()

# Display results
print("📊 Average Salaries Across All Majors:")
for col, avg in average_salaries.items():
    print(f"{col}: ${avg:,.2f}")