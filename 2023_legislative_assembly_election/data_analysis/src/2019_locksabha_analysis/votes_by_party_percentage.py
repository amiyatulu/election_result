import json

# Assuming your JSON file is named 'votes_data.json'
json_file_path = 'analysis_data/lokshabha2019/state_party_data_sorted/party_votes_by_state_sorted.json'

json_directory_path = "analysis_data/lokshabha2019/state_party_data_sorted_percentage/"


# Read the JSON data from the file
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# Calculate the percentage for each party within each state
for state, party_data in data.items():
    total_votes_state = sum(party_data.values())
    for party, votes in party_data.items():
        data[state][party] = {
            'votes': votes,
            'percentage': (votes / total_votes_state) * 100 if total_votes_state != 0 else 0
        }

# Print the updated data with percentage
print(json.dumps(data, indent=2))

# Save the sorted result_dict to a JSON file
with open(json_directory_path + 'party_votes_by_state_percentage.json', 'w') as json_file:
    json.dump(data, json_file, indent=2)

print("JSON file created for party votes by state (sorted).")
