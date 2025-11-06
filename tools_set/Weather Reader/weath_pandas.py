import pandas

data = pandas.read_csv("./weather_data.csv")

temperature = data["temp"].to_list()
x_bar = sum(temperature) / len(temperature)
print(f"Mean temperature: {x_bar}")

maxtemp = data["temp"].max()
print(f"Max value of temperature is {maxtemp}")

# ✅ Show row(s) with max temperature
print(data[data["temp"] == maxtemp])