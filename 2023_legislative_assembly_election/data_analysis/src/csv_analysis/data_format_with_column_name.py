import pandas as pd
import snake_case

file_path = 'data/UP_election/10-Detailed Results.csv'

# Skip the first three rows and use the 4th row as headers
df = pd.read_csv(file_path, skiprows=3)

print(df.head())

# Filter rows where the first column is "Uttar Pradesh"
data = df[df.iloc[:, 0] == 'Uttar Pradesh']

# Display the resulting DataFrame
print(data["AC NAME"])


constituencies = df["AC NAME"]
num_constituencies = df["AC NAME"].nunique()
print(num_constituencies)

constituency = df[df["AC NAME"] == "Behat"]
print(constituency)

max_votes_candidate = constituency.loc[constituency['TOTAL'].idxmax(), 'CANDIDATE NAME']

print(f"The candidate with the highest votes in Behat constituency is: {max_votes_candidate}")


winning_candidate_row = constituency.loc[constituency['TOTAL'].idxmax()]

print("Row with the highest TOTAL:")
print(winning_candidate_row)

print("Votes of Winning candidata")
print(winning_candidate_row['TOTAL'])


# Sum votes for all candidates other than the winning candidate
sum_votes_other_than_winner = constituency.loc[constituency['CANDIDATE NAME'] != winning_candidate_row['CANDIDATE NAME'], 'TOTAL'].sum()

print(f"The sum of all votes other than the winning candidate in Behat constituency is: {sum_votes_other_than_winner}")
