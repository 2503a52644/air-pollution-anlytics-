import pandas as pd

# Read cleaned CSV file
df = pd.read_csv("cleaned_city_day_data.csv")

# Show column names
print("Column Names:")
print(df.columns)

# Show first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nDataset Shape:")
print(df.shape)

print("\nStatistical Summary:")
print(df.describe())

import pandas as pd

# Read cleaned CSV file
df = pd.read_csv("cleaned_city_day_data.csv")

# AQI Analysis
print("\n----- AQI ANALYSIS -----")

print("\nAverage AQI:")
print(df["AQI"].mean())

print("\nMaximum AQI:")
print(df["AQI"].max())

print("\nMinimum AQI:")
print(df["AQI"].min())


# City-wise AQI Analysis

print("\n----- CITY-WISE AQI ANALYSIS -----")

city_aqi = df.groupby("City")["AQI"].mean()

print("\nAverage AQI of Each City:")
print(city_aqi)

# Find the most polluted city

most_polluted_city = city_aqi.idxmax()
highest_aqi = city_aqi.max()

print("\n----- MOST POLLUTED CITY -----")
print("City:", most_polluted_city)
print("Average AQI:", highest_aqi)

# Find the least polluted city

least_polluted_city = city_aqi.idxmin()
lowest_aqi = city_aqi.min()

print("\n----- LEAST POLLUTED CITY -----")
print("City:", least_polluted_city)
print("Average AQI:", lowest_aqi)

# ----- POLLUTANT ANALYSIS -----

print("\n----- POLLUTANT ANALYSIS -----")

pollutants = [
    "PM2.5", "PM10", "NO", "NO2", "NOx",
    "NH3", "CO", "SO2", "O3",
    "Benzene", "Toluene", "Xylene"
]

# Calculate average pollutant values
average_pollutants = df[pollutants].mean()

print("\nAverage Value of Each Pollutant:")
print(average_pollutants)

# Find the pollutant with the highest average value

highest_pollutant = average_pollutants.idxmax()
highest_value = average_pollutants.max()

print("\n----- HIGHEST POLLUTANT -----")
print("Pollutant:", highest_pollutant)
print("Average Value:", highest_value)
print("\n========== FINAL INSIGHTS ==========")

print(f"\nOverall Average AQI: {df['AQI'].mean():.2f}")
print(f"Highest AQI Recorded: {df['AQI'].max()}")
print(f"Lowest AQI Recorded: {df['AQI'].min()}")

print(f"\nMost Polluted City: {most_polluted_city}")
print(f"Highest City Average AQI: {highest_aqi:.2f}")

print(f"\nLeast Polluted City: {least_polluted_city}")
print(f"Lowest City Average AQI: {lowest_aqi:.2f}")

print(f"\nHighest Average Pollutant: {highest_pollutant}")
print(f"Average Value: {highest_value:.2f}")

print("\nAnalysis completed successfully!")