import pandas as pd

# Read CSV file
df = pd.read_csv("city_day.csv")

# Display first 5 rows
print("Original Data:")
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

# Save cleaned data as CSV
df.to_csv("cleaned_city_day_data.csv", index=False)

print("\nData cleaned successfully!")
print("Cleaned file saved as cleaned_aqi_data.csv")