import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("space_missions.csv")  # Replace with your actual file path

# Preprocess
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.dropna(subset=["Date"])
df["Year"] = df["Date"].dt.year

# === 1. Launches per Year ===
launches_per_year = df["Year"].value_counts().sort_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x=launches_per_year.index, y=launches_per_year.values, marker="o")
plt.title("🚀 Space Launches per Year (1957–Present)")
plt.xlabel("Year")
plt.ylabel("Number of Launches")
plt.grid(True)
plt.tight_layout()
plt.show()

# === 2. Top 10 Countries by Launches ===
top_countries = df["Country"].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette="viridis")
plt.title("🌍 Top 10 Launching Countries")
plt.xlabel("Total Launches")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

# === 3. Mission Status Trends ===
status_by_year = df.groupby(["Year", "Mission_Status"]).size().unstack(fill_value=0)

plt.figure(figsize=(12, 6))
status_by_year.plot(kind="bar", stacked=True, colormap="Set2", figsize=(12, 6))
plt.title("📊 Mission Status Trends Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Missions")
plt.legend(title="Status")
plt.tight_layout()
plt.show()