import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)
df["PRICE"] = boston.target

# 1️⃣ Explore data
print(df.head())
sns.pairplot(df[["RM", "LSTAT", "PTRATIO", "DIS", "PRICE"]])
plt.show()

# 2️⃣ Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("📊 Feature Correlation with Price")
plt.show()

# 3️⃣ Split data
X = df.drop("PRICE", axis=1)
y = df["PRICE"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4️⃣ Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5️⃣ Train model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# 6️⃣ Evaluate model
y_pred = model.predict(X_test_scaled)
print("📈 Coefficients:", model.coef_)
print("📊 Intercept:", model.intercept_)
print("✅ R² Score:", r2_score(y_test, y_pred))
print("📉 RMSE:", mean_squared_error(y_test, y_pred, squared=False))

# 7️⃣ Residual plot
residuals = y_test - y_pred
plt.figure(figsize=(8, 5))
sns.histplot(residuals, bins=30, kde=True)
plt.title("📉 Residual Distribution")
plt.xlabel("Residuals")
plt.show()

# 8️⃣ Predict new property
sample = pd.DataFrame([{
    "CRIM": 0.1,      # Crime rate
    "ZN": 0,          # Residential land zoned
    "INDUS": 7.0,     # Industrial proportion
    "CHAS": 0,        # Charles River dummy
    "NOX": 0.5,       # Nitric oxide concentration
    "RM": 6.5,        # Average rooms
    "AGE": 50,        # Age of property
    "DIS": 4.0,       # Distance to employment centers
    "RAD": 4,         # Accessibility to highways
    "TAX": 300,       # Property tax rate
    "PTRATIO": 18.0,  # Student-teacher ratio
    "B": 390.0,       # Proportion of Black residents
    "LSTAT": 12.0     # % lower status population
}])
sample_scaled = scaler.transform(sample)
predicted_price = model.predict(sample_scaled)[0]
print(f"🏡 Estimated Property Price: ${predicted_price * 1000:,.2f}")