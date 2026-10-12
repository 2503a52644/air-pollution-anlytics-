
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Read the cleaned dataset
df = pd.read_csv("cleaned_city_day_data.csv")

# Create a folder for the charts
Path("charts").mkdir(exist_ok=True)

# Convert AQI and pollutant columns to numeric values
numeric_columns = [
    "AQI", "PM2.5", "PM10", "NO", "NO2", "NOx",
    "NH3", "CO", "SO2", "O3", "Benzene",
    "Toluene", "Xylene"
]

for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# ---------------------------------
# CHART 1: City-wise Average AQI
# ---------------------------------
if {"City", "AQI"}.issubset(df.columns):
    city_aqi = df.groupby("City")["AQI"].mean().dropna()
    city_aqi = city_aqi.sort_values(ascending=False)

    plt.figure(figsize=(12, 6))
    city_aqi.plot(kind="bar")
    plt.title("City-wise Average AQI")
    plt.xlabel("City")
    plt.ylabel("Average AQI")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("charts/city_wise_aqi.png", dpi=150)
    plt.show()
    plt.close()

# ---------------------------------
# CHART 2: AQI Trend Over Time
# ---------------------------------
if {"Date", "AQI"}.issubset(df.columns):
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    trend = df.dropna(subset=["Date", "AQI"])
    trend = trend.groupby("Date")["AQI"].mean().sort_index()

    if not trend.empty:
        plt.figure(figsize=(12, 6))
        plt.plot(trend.index, trend.values, marker="o",
                 markersize=3)
        plt.title("Average AQI Trend Over Time")
        plt.xlabel("Date")
        plt.ylabel("Average AQI")
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig("charts/aqi_trend.png", dpi=150)
        plt.show()
        plt.close()

# ---------------------------------
# CHART 3: Average Pollutant Levels
# ---------------------------------
pollutants = [
    col for col in numeric_columns
    if col not in ["AQI"] and col in df.columns
]

if pollutants:
    averages = df[pollutants].mean().dropna()
    averages = averages.sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    averages.plot(kind="bar")
    plt.title("Average Pollutant Levels")
    plt.xlabel("Pollutant")
    plt.ylabel("Average Recorded Value")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("charts/pollutant_comparison.png", dpi=150)
    plt.show()
    plt.close()

# ---------------------------------
# CHART 4: AQI Category Distribution
# ---------------------------------
if "AQI_Bucket" in df.columns:
    categories = df["AQI_Bucket"].dropna().value_counts()

    if not categories.empty:
        plt.figure(figsize=(8, 8))
        categories.plot(
            kind="pie",
            autopct="%1.1f%%",
            startangle=90
        )
        plt.title("AQI Category Distribution")
        plt.ylabel("")
        plt.tight_layout()
        plt.savefig("charts/aqi_categories.png", dpi=150)
        plt.show()
        plt.close()

print("Data visualization completed!")
print("Check the charts folder for your saved images.")
