import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
sets = pd.read_csv("sets.csv")
themes = pd.read_csv("themes.csv")

# Merge sets with themes
lego = pd.merge(sets, themes, how="left", left_on="theme_id", right_on="id")

# 1️⃣ Most enormous LEGO set
largest_set = lego.loc[lego["num_parts"].idxmax()]
print(f"🧱 Largest set: {largest_set['name']} with {largest_set['num_parts']} parts")

# 2️⃣ First LEGO sets released
first_year = lego["year"].min()
first_year_sets = lego[lego["year"] == first_year]
print(f"📅 First year: {first_year}, Sets released: {len(first_year_sets)}")

# 3️⃣ Theme with most sets
theme_counts = lego["name_y"].value_counts()
top_theme = theme_counts.idxmax()
print(f"🎭 Most popular theme: {top_theme} with {theme_counts.max()} sets")

# 4️⃣ LEGO growth over time
sets_per_year = lego.groupby("year").agg({"set_num": "count", "name_y": "nunique"}).rename(columns={"set_num": "num_sets", "name_y": "num_themes"})
sets_per_year.plot(kind="line", figsize=(12, 6), title="LEGO Growth Over Time")
plt.xlabel("Year")
plt.ylabel("Count")
plt.grid(True)
plt.tight_layout()
plt.show()

# 5️⃣ Complexity over time
avg_parts_per_year = lego.groupby("year")["num_parts"].mean()
avg_parts_per_year.plot(kind="scatter", figsize=(12, 6), title="Average Parts per Set Over Time")
plt.xlabel("Year")
plt.ylabel("Average Number of Parts")
plt.grid(True)
plt.tight_layout()
plt.show()