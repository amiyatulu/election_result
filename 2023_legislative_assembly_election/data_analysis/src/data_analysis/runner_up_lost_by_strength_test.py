import pandas as pd

import json


json_file_path = "data/madhya_pradesh/constituency_data_all.json"

df = pd.read_json(json_file_path)

# print(df)

constituencies = df["Constituency"]
num_constituencies = df['Constituency'].nunique()

candidate_infos = df[df["Constituency"] == "Alirajpur - 191"]["Candidates_info"]

won_candidates = candidate_infos.apply(lambda x: [candidate for candidate in x if candidate['Status'] == 'won'])

lost_candidates = candidate_infos.apply(lambda x: [candidate for candidate in x if candidate['Status'] == 'lost'])
print(lost_candidates)

candidate_info_info = lost_candidates.iloc[0]

print(candidate_info_info)


# Initialize variables to keep track of the candidate with the highest votes
highest_votes_candidate = None
highest_votes = 0

# Loop through the list of lost candidates
for candidate in candidate_info_info:
    # Extract 'Votes' value for the current candidate and convert it to an integer
    votes = int(candidate['Votes'])
    
    # Check if the current candidate has more votes than the current highest
    if votes > highest_votes:
        highest_votes = votes
        highest_votes_candidate = candidate

# Display the result
print("Lost candidate with the highest votes:")
print(highest_votes_candidate)
print(highest_votes_candidate["Votes"])