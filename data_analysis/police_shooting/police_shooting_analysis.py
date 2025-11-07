import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
shootings = pd.read_csv("fatal-police-shootings-data.csv")  # Washington Post dataset
census = pd.read_csv("us_census_data.csv")  # Custom census data by state

# Preprocess
shootings["year"] = pd.to_datetime(shootings["date"]).dt.year
shootings = shootings[shootings["year"] >= 2015]

# Aggregate shootings by state
state_counts = shootings["state"].value_counts().reset_index()
state_counts.columns = ["state", "shooting_count"]

# Merge with census data
merged = pd.merge(census, state_counts, on="state", how="left")
merged["shooting_count"] = merged["shooting_count"].fillna(0)

# Normalize by population
merged["shootings_per_million"] = (merged["shooting_count"] / merged["population"]) * 1_000_000

# Correlation analysis
corr = merged[["poverty_rate", "high_school_grad_rate", "black_pct", "shootings_per_million"]].corr()

# === 1. Heatmap of Correlations ===
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("📊 Correlation Between Social Factors and Police Shootings")
plt.tight_layout()
plt.show()

# === 2. Scatter Plot: Poverty vs Shootings ===
plt.figure(figsize=(8, 6))
sns.scatterplot(data=merged, x="poverty_rate", y="shootings_per_million", hue="black_pct", size="population", palette="viridis")
plt.title("💸 Poverty Rate vs Police Shootings per Million")
plt.xlabel("Poverty Rate (%)")
plt.ylabel("Shootings per Million People")
plt.tight_layout()
plt.show()

# === 3. Top 10 States by Shooting Rate ===
top_states = merged.sort_values("shootings_per_million", ascending=False).head(10)
print("🔝 Top 10 States by Police Shootings per Million:")
print(top_states[["state", "shootings_per_million", "poverty_rate", "black_pct"]])