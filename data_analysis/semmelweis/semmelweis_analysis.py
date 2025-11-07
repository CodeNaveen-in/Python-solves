import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# Load data
df = pd.read_csv("semmelweis.csv")
df["Mortality Rate"] = df["Deaths"] / df["Births"]

# Split by clinic
clinic1 = df[df["Clinic"] == 1]
clinic2 = df[df["Clinic"] == 2]

# 1️⃣ Superimposed histograms
plt.figure(figsize=(10, 6))
sns.histplot(clinic1["Mortality Rate"], color="red", label="Clinic 1", kde=False, bins=10)
sns.histplot(clinic2["Mortality Rate"], color="blue", label="Clinic 2", kde=False, bins=10)
plt.title("🧪 Mortality Rate Distribution by Clinic")
plt.xlabel("Mortality Rate")
plt.legend()
plt.show()

# 2️⃣ KDE plot
plt.figure(figsize=(10, 6))
sns.kdeplot(clinic1["Mortality Rate"], shade=True, label="Clinic 1", color="red")
sns.kdeplot(clinic2["Mortality Rate"], shade=True, label="Clinic 2", color="blue")
plt.title("📈 KDE of Mortality Rates")
plt.xlabel("Mortality Rate")
plt.legend()
plt.show()

# 3️⃣ Statistical significance
t_stat, p_val = ttest_ind(clinic1["Mortality Rate"], clinic2["Mortality Rate"])
print(f"📊 T-test p-value: {p_val:.4f}")
if p_val < 0.05:
    print("✅ Statistically significant difference in mortality rates between clinics.")

# 4️⃣ Highlight handwashing intervention (mid-1847)
df["Handwashing"] = np.where(df["Year"] >= 1847, "After", "Before")

plt.figure(figsize=(12, 6))
for label, group in df.groupby("Handwashing"):
    plt.plot(group["Year"], group["Mortality Rate"], label=f"{label} Handwashing", marker="o")

plt.axvline(x=1847, color="green", linestyle="--", label="🧼 Handwashing Introduced")
plt.title("📉 Mortality Rate Over Time")
plt.xlabel("Year")
plt.ylabel("Mortality Rate")
plt.legend()
plt.grid(True)
plt.show()