import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2.csv", skiprows=4)

# Select latest year population data
population_data = df["2023"]

# Remove missing values
population_data = population_data.dropna()

# Create histogram
plt.figure(figsize=(10,6))
plt.hist(population_data, bins=20, edgecolor='black')

# Labels and title
plt.title("Distribution of Population Across Countries (2023)")
plt.xlabel("Population")
plt.ylabel("Number of Countries")

# Show graph
plt.show()