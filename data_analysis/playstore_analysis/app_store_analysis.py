import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load and clean data
df = pd.read_csv("playstore.csv")
df.drop_duplicates(subset="App", inplace=True)
df["Installs"] = df["Installs"].str.replace(r"[+,]", "", regex=True).astype(int)
df["Price"] = df["Price"].str.replace("$", "").astype(float)
df["Reviews"] = pd.to_numeric(df["Reviews"], errors="coerce")
df["Type"] = df["Type"].fillna("Free")

# 1️⃣ Most competitive categories
category_counts = df["Category"].value_counts().reset_index()
fig1 = px.bar(category_counts, x="index", y="Category", title="Number of Apps per Category", labels={"index": "Category", "Category": "App Count"})
fig1.show()

# 2️⃣ Most popular categories by installs
category_installs = df.groupby("Category")["Installs"].sum().sort_values(ascending=False).reset_index()
fig2 = px.bar(category_installs.head(10), x="Category", y="Installs", title="Top 10 Categories by Total Installs")
fig2.show()

# 3️⃣ Free vs Paid: Downloads
type_installs = df.groupby("Type")["Installs"].sum().reset_index()
fig3 = px.pie(type_installs, names="Type", values="Installs", title="Free vs Paid App Installs", hole=0.4)
fig3.show()

# 4️⃣ Price distribution of paid apps
paid_apps = df[df["Type"] == "Paid"]
fig4 = px.histogram(paid_apps, x="Price", nbins=30, title="Price Distribution of Paid Apps")
fig4.show()

# 5️⃣ Top revenue-generating paid apps
paid_apps["Revenue"] = paid_apps["Price"] * paid_apps["Installs"]
top_revenue = paid_apps.sort_values("Revenue", ascending=False).head(10)
fig5 = px.bar(top_revenue, x="App", y="Revenue", title="Top 10 Revenue-Generating Paid Apps")
fig5.show()

# 6️⃣ Revenue vs Development Cost (assume $10,000 cost)
paid_apps["Profitable"] = paid_apps["Revenue"] > 10000
profit_counts = paid_apps["Profitable"].value_counts().reset_index()
fig6 = px.pie(profit_counts, names="index", values="Profitable", title="Paid Apps That Recouped $10K Dev Cost", hole=0.3)
fig6.show()