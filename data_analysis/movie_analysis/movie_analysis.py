import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Load data
df = pd.read_csv("movies.csv")

# Clean and prepare
df.dropna(subset=["Budget", "Revenue"], inplace=True)
df["Budget_M"] = df["Budget"] // 1_000_000
df["Revenue_M"] = df["Revenue"] // 1_000_000

# 1️⃣ Scatter plot with regression line
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.regplot(x="Budget_M", y="Revenue_M", data=df, scatter_kws={"s": 100}, line_kws={"color": "red"})
plt.title("🎬 Do Bigger Budgets Lead to Bigger Box Office?")
plt.xlabel("Budget (in Millions USD)")
plt.ylabel("Revenue (in Millions USD)")
plt.show()

# 2️⃣ Linear regression with scikit-learn
X = df[["Budget"]]
y = df["Revenue"]
model = LinearRegression()
model.fit(X, y)
print(f"📈 Coefficient: {model.coef_[0]:,.2f}")
print(f"📊 Intercept: {model.intercept_:,.2f}")
print(f"R² Score: {model.score(X, y):.2f}")

# 3️⃣ Bubble chart: Budget vs Revenue, bubble size = Rating
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Budget_M", y="Revenue_M", size="Rating", hue="Rating", data=df, palette="coolwarm", sizes=(100, 1000), legend=False)
plt.title("🎈 Bubble Chart: Budget vs Revenue (Bubble = IMDb Rating)")
plt.xlabel("Budget (in Millions USD)")
plt.ylabel("Revenue (in Millions USD)")
plt.grid(True)
plt.show()

# 4️⃣ Grouping by budget bins using floor division
df["Budget_Bin"] = df["Budget"] // 100_000_000 * 100  # e.g., 0-99M, 100-199M, etc.
grouped = df.groupby("Budget_Bin")["Revenue"].mean().reset_index()

# Bar chart of average revenue by budget bin
plt.figure(figsize=(8, 5))
sns.barplot(x="Budget_Bin", y="Revenue", data=grouped, palette="Blues_d")
plt.title("💰 Average Revenue by Budget Bin")
plt.xlabel("Budget Bin (in $100M)")
plt.ylabel("Average Revenue")
plt.show()