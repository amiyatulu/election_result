import pandas as pd

import json


json_file_path = "data/madhya_pradesh/constituency_data_all.json"

df = pd.read_json(json_file_path)

# print(df)

constituencies = df["Constituency"]
num_constituencies = df['Constituency'].nunique()

# print(constituencies.to_dict())

vote_wastage_data = []

number_of_places_vote_waste_won = 0

for constituency in constituencies:
    # print(constituency)
    candidate_infos = df[df["Constituency"] == constituency]["Candidates_info"]

    won_candidates = candidate_infos.apply(lambda x: [candidate for candidate in x if candidate['Status'] == 'won'])
    # print(won_candidates)

    # print(won_candidates.to_dict()[0][0]["Votes"])

    lost_candidates = candidate_infos.apply(lambda x: [candidate for candidate in x if candidate['Status'] == 'lost'])
    print(lost_candidates.to_dict())

    lost_candidates_votes = lost_candidates.apply(lambda x: [item['Votes'] for item in x])
    # print()

    total_sum = sum(map(int, lost_candidates_votes.sum()))
    print(total_sum)

    # Display the result
    # print(f"Sum of the values: {total_sum}")

    winner_info = won_candidates.iloc[0]
    winner_votes_int = int(winner_info[0]["Votes"])
    if total_sum > winner_votes_int:
        number_of_places_vote_waste_won = number_of_places_vote_waste_won + 1


    wastage = {
        "Constituency": constituency,
        "Winner": winner_info[0]["Candidate Name"],
        "Winner Party": winner_info[0]["Party"],
        "Winner Votes": winner_votes_int,
        "Vote Wastage": total_sum
    }

    vote_wastage_data.append(wastage)

total_data = {
    "No of constituency where vote wastage won": number_of_places_vote_waste_won,
    "No of constituency" : num_constituencies,
    "Constituency data": vote_wastage_data
}

json_data = json.dumps(total_data, indent=2)

json_file_path = 'vote_wastage_data_madhay_pradesh.json'

# Save the JSON data to a file
with open(json_file_path, 'w') as json_file:
    json_file.write(json_data)

print(f"JSON data saved to {json_file_path}")
