import pandas as pd

# Load the dataset
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Count squirrels by primary fur color
fur_counts = data["Primary Fur Color"].value_counts()

# Convert to DataFrame
fur_df = fur_counts.reset_index()
fur_df.columns = ["Fur Color", "Count"]

# Save to CSV
fur_df.to_csv("squirrel_fur_color_count.csv", index=False)

print("Squirrel fur color counts saved to 'squirrel_fur_color_count.csv'")