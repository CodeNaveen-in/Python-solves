import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("language_popularity.csv")

# Set 'Year' as index for easier plotting
df.set_index("Year", inplace=True)

# Plotting
plt.figure(figsize=(12, 6))
for language in df.columns:
    plt.plot(df.index, df[language], label=language, linewidth=2)

plt.title("📈 Popularity of Programming Languages Over Time")
plt.xlabel("Year")
plt.ylabel("Popularity Score")
plt.legend(title="Languages")
plt.grid(True)
plt.tight_layout()
plt.show()