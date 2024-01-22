import pandas as pd
import json

json_file_path = "data/constituency_data_mizoram.json"
df = pd.read_json(json_file_path)

votes_by_party = {}

for index, row in df.iterrows():
    candidates_info = row["Candidates_info"]

    for candidate in candidates_info:
        party = candidate["Party"]
        votes = int(candidate["Votes"])

        if party in votes_by_party:
            votes_by_party[party] += votes
        else:
            votes_by_party[party] = votes

total_data = {
    "VotesByParty": votes_by_party
}

json_data = json.dumps(total_data, indent=2)

json_file_path = 'analysis_data/total_votes_by_party_data/total_votes_by_party_data_mizoram.json'

# Save the JSON data to a file
with open(json_file_path, 'w') as json_file:
    json_file.write(json_data)

print(f"JSON data saved to {json_file_path}")
