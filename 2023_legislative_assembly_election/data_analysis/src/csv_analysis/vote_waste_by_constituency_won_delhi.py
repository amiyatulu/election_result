import pandas as pd
import json

from snake_case import to_snake_case, clean_candidate_name


file_path = 'data/delhi/10-Detailed Results_Delhi_General_Legislative_Election_2020.csv'
election_title = "Delhi Legislative Election 2020"
state_name = "NCT OF Delhi"
election_title_snake = to_snake_case(election_title)

# Skip the first three rows and use the 4th row as headers
df = pd.read_csv(file_path, skiprows=2)

df.columns = df.columns.str.strip()

print(df.head())

# Filter rows where the first column is "Uttar Pradesh"
data = df[df.iloc[:, 0] == state_name]

# Display the resulting DataFrame
# print(data["AC NAME"])


# constituencies = data["AC NAME"]
num_constituencies = data["AC NAME"].nunique()
print(num_constituencies)

constituencies = data["AC NAME"].unique()
print(constituencies)



vote_wastage_data = []

number_of_places_vote_waste_won = 0

for constituency in constituencies:
    constituency_data = data[data["AC NAME"] == constituency]
    # max_votes_candidate = constituency.loc[constituency['TOTAL'].idxmax(), 'CANDIDATE NAME']
    # print(f"The candidate with the highest votes in Behat constituency is: {max_votes_candidate}")
    winning_candidate_row = constituency_data.loc[constituency_data['TOTAL'].idxmax()]
    print(winning_candidate_row)

    # print("Row with the highest TOTAL:")
    # print(winning_candidate_row)


    # Sum votes for all candidates other than the winning candidate
    sum_votes_other_than_winner = constituency_data.loc[constituency_data['CANDIDATE NAME'] != winning_candidate_row['CANDIDATE NAME'], 'TOTAL'].sum()

    # print(f"The sum of all votes other than the winning candidate in Behat constituency is: {sum_votes_other_than_winner}")
    if sum_votes_other_than_winner > winning_candidate_row['TOTAL']:
        number_of_places_vote_waste_won = number_of_places_vote_waste_won + 1
        wastage = {
        "Constituency": constituency,
        "Winner": clean_candidate_name(winning_candidate_row['CANDIDATE NAME']),
        "Winner Party": winning_candidate_row["PARTY"],
        "Winner Votes": winning_candidate_row['TOTAL'],
        "Vote Wastage": sum_votes_other_than_winner
        }
        vote_wastage_data.append(wastage)

total_data = {
    "Election": election_title,
    "No of constituency where vote wastage won": number_of_places_vote_waste_won,
    "No of constituency" : num_constituencies,
    "Constituency data where vote wastage won": vote_wastage_data
}

json_data = json.dumps(total_data, indent=2)

json_file_path = f'analysis_data/vote_wastage_won_data/vote_wastage_data_{election_title_snake}.json'

# Save the JSON data to a file
with open(json_file_path, 'w') as json_file:
    json_file.write(json_data)

print(f"JSON data saved to {json_file_path}")






