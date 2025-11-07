import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("nobel_prizes_1901-2025_cleaned.csv")
df.dropna(subset=["Year", "Category", "Gender", "Birth Country"], inplace=True)

# 1️⃣ Choropleth: Nobel laureates by country
country_counts = df["Birth Country"].value_counts().reset_index()
country_counts.columns = ["Country", "Laureates"]
fig1 = px.choropleth(country_counts, locations="Country", locationmode="country names",
                     color="Laureates", title="🌍 Nobel Laureates by Country", color_continuous_scale="Viridis")
fig1.show()

# 2️⃣ Bar chart: Gender distribution by category
gender_cat = df.groupby(["Category", "Gender"]).size().reset_index(name="Count")
fig2 = px.bar(gender_cat, x="Category", y="Count", color="Gender", barmode="group",
              title="👩‍🔬 Gender Distribution by Nobel Category")
fig2.show()

# 3️⃣ Sunburst chart: Category → Gender → Country
fig3 = px.sunburst(df, path=["Category", "Gender", "Birth Country"], title="🌞 Nobel Prize Breakdown")
fig3.show()

# 4️⃣ Seaborn lmplot: Year vs Age with category hue
df["Birth Year"] = pd.to_datetime(df["Birth Date"], errors="coerce").dt.year
df["Age"] = df["Year"] - df["Birth Year"]
sns.lmplot(data=df, x="Year", y="Age", hue="Category", lowess=True, height=6, aspect=1.5)
plt.title("📈 Age of Nobel Laureates Over Time by Category")
plt.show()

# 5️⃣ Box plot vs time series: Age distribution vs trend
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x="Category", y="Age")
plt.title("📦 Age Distribution by Nobel Category")
plt.show()

df_yearly = df.groupby("Year")["Age"].mean().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_yearly, x="Year", y="Age")
plt.title("📊 Average Age of Laureates Over Time")
plt.show()

# 6️⃣ Histogram: Age distribution
plt.figure(figsize=(10, 5))
sns.histplot(df["Age"].dropna(), bins=30, kde=True)
plt.title("🎂 Distribution of Laureate Ages")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()