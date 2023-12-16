import pandas as pd

file_path = 'data/UP_election/10-Detailed Results.csv'

df = pd.read_csv(file_path)

print(df.head())

# Filter rows where the first column is "Uttar Pradesh"
uttar_pradesh_data = df[df.iloc[:, 0] == 'Uttar Pradesh']

# Display the resulting DataFrame
print(uttar_pradesh_data)