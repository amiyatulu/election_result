import pandas as pd
import json
import numpy as np


# Assuming your data is in a CSV file named 'election_data.csv'
df = pd.read_csv('data/loksabha2019/Constituency_Wise_Detailed_Result_General Election_2019.csv', skiprows=2)

json_directory_path = "analysis_data/lokshabha2019/state_party_data_sorted/"

df.columns = df.columns.str.strip()

# Group the data by State Name and Party Name
grouped_data = df.groupby(['State Name', 'PARTY NAME'])


# Dictionary to store the results
result_dict = {}

# Iterate through each group (state and party) and sum the votes
for (state, party), data in grouped_data:
    total_votes = data['TOTAL'].sum()

    # If state not in result_dict, add it
    if state not in result_dict:
        result_dict[state] = {}

    # Convert non-string keys to strings
    key = str(party)

    # Convert numpy.int64 to int before adding to dictionary
    total_votes = int(total_votes) if not np.isnan(total_votes) else 0

    # Add party votes to the state
    result_dict[state][key] = total_votes


# Sort the parties within each state based on total votes in descending order
for state, party_votes in result_dict.items():
    result_dict[state] = dict(sorted(party_votes.items(), key=lambda x: x[1], reverse=True))

# Print the sorted result_dict
print(json.dumps(result_dict, indent=2))

# Save the sorted result_dict to a JSON file
with open(json_directory_path + 'party_votes_by_state_sorted.json', 'w') as json_file:
    json.dump(result_dict, json_file, indent=2)

print("JSON file created for party votes by state (sorted).")
