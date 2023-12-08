import pandas as pd

import json


json_file_path = "data/constituency_data_mizoram.json"

df = pd.read_json(json_file_path)


constituencies = df["Constituency"]
num_constituencies = df['Constituency'].nunique()



runner_up_data = []

counter = {"1000": 0, "2000": 0, "3000": 0, "4000": 0, "5000": 0, "6000": 0, "7000": 0, "8000": 0, "9000": 0, "10000": 0, ">10000": 0, "20000": 0, "30000":0, "40000": 0, ">40000": 0}



runner_up_strength_data = {"runner_up_less_than_1000": [], "runner_up_less_than_2000_more_than_1000": [], "runner_up_less_than_3000_more_than_2000": [], "runner_up_less_than_4000_more_than_3000": [], "runner_up_less_than_5000_more_than_4000": [], "runner_up_less_than_6000_more_than_5000": [], "runner_up_less_than_7000_more_than_6000": [], "runner_up_less_than_8000_more_than_7000": [], "runner_up_less_than_9000_more_than_8000": [], "runner_up_less_than_10000_more_than_9000": [], "runner_up_less_than_20000_more_than_10000": [], "runner_up_less_than_30000_more_than_20000":[], "runner_up_less_than_40000_more_than_30000": [], ">40000": [],  ">10000": []}


for constituency in constituencies:

    candidate_infos = df[df["Constituency"] == constituency]["Candidates_info"]

    won_candidates = candidate_infos.apply(lambda x: [candidate for candidate in x if candidate['Status'] == 'won'])
    
    lost_candidates = candidate_infos.apply(lambda x: [candidate for candidate in x if candidate['Status'] == 'lost'])

    lost_candidate__info = lost_candidates.iloc[0]

    # Initialize variables to keep track of the candidate with the highest votes
    highest_votes_runner_up_candidate = None
    highest_votes = 0

    # Loop through the list of lost candidates
    for candidate in lost_candidate__info:
        # Extract 'Votes' value for the current candidate and convert it to an integer
        votes = int(candidate['Votes'])
        
        # Check if the current candidate has more votes than the current highest
        if votes > highest_votes:
            highest_votes = votes
            highest_votes_runner_up_candidate = candidate

    # Display the result
    # print("Lost candidate with the highest votes:")
    # print(highest_votes_runner_up_candidate)

    winner_info = won_candidates.iloc[0]
    winner_votes_int = int(winner_info[0]["Votes"])

    first_runner_up_vote = int(highest_votes_runner_up_candidate["Votes"])

    winner_own_by = winner_votes_int - first_runner_up_vote

    runner_up = {
        "Constituency": constituency,
        "Winner": winner_info[0]["Candidate Name"],
        "Winner Party": winner_info[0]["Party"],
        "Winner Votes": winner_votes_int,
        "Runner Up": highest_votes_runner_up_candidate['Candidate Name'],
        "Runner Up Party": highest_votes_runner_up_candidate["Party"],
        "Runner Up Votes": first_runner_up_vote, 
    }
    if winner_own_by < 1000:
        counter["1000"] = counter["1000"] + 1
        runner_up_strength_data['runner_up_less_than_1000'].append(runner_up)
    if winner_own_by < 2000 and winner_own_by >=1000:
        counter["2000"] = counter["2000"] + 1
        runner_up_strength_data['runner_up_less_than_2000_more_than_1000'].append(runner_up)
    if winner_own_by < 3000 and winner_own_by >= 2000:
        counter["3000"] = counter["3000"] + 1
        runner_up_strength_data['runner_up_less_than_3000_more_than_2000'].append(runner_up)
    if winner_own_by < 4000 and winner_own_by >= 3000:
        counter["4000"] = counter["4000"] + 1
        runner_up_strength_data['runner_up_less_than_4000_more_than_3000'].append(runner_up)
    if winner_own_by < 5000 and winner_own_by >= 4000:
        counter["5000"] = counter["5000"] + 1
        runner_up_strength_data['runner_up_less_than_5000_more_than_4000'].append(runner_up)
    if winner_own_by < 6000 and winner_own_by >= 5000:
        counter["6000"] = counter["6000"] + 1
        runner_up_strength_data['runner_up_less_than_6000_more_than_5000'].append(runner_up)
    if winner_own_by < 7000 and winner_own_by >= 6000:
        counter["7000"] = counter["7000"] + 1
        runner_up_strength_data['runner_up_less_than_7000_more_than_6000'].append(runner_up)
    if winner_own_by < 8000 and winner_own_by >= 7000:
        counter["8000"] = counter["8000"] + 1
        runner_up_strength_data['runner_up_less_than_8000_more_than_7000'].append(runner_up)
    if winner_own_by < 9000 and winner_own_by >= 8000:
        counter["9000"] = counter["9000"] + 1
        runner_up_strength_data['runner_up_less_than_9000_more_than_8000'].append(runner_up)
    if winner_own_by < 10000 and winner_own_by >= 9000:
        counter["10000"] = counter["10000"] + 1
        runner_up_strength_data['runner_up_less_than_10000_more_than_9000'].append(runner_up)
    if winner_own_by >= 10000:
        counter[">10000"] = counter[">10000"] + 1
        runner_up_strength_data['>10000'].append(runner_up)
    if winner_own_by < 20000 and winner_own_by >= 10000:
        counter["20000"]  = counter["20000"] + 1
        runner_up_strength_data['runner_up_less_than_20000_more_than_10000'].append(runner_up)
    if winner_own_by < 30000 and winner_own_by >= 20000:
        counter["30000"]  = counter["30000"] + 1
        runner_up_strength_data['runner_up_less_than_30000_more_than_20000'].append(runner_up)
    if winner_own_by < 40000 and winner_own_by >= 30000:
        counter["40000"]  = counter["40000"] + 1
        runner_up_strength_data['runner_up_less_than_40000_more_than_30000'].append(runner_up)
    if winner_own_by >= 40000:
        counter[">40000"]  = counter[">40000"] + 1
        runner_up_strength_data['>40000'].append(runner_up)




    # runner_up = {
    #     "Constituency": constituency,
    #     "Winner": winner_info[0]["Candidate Name"],
    #     "Winner Party": winner_info[0]["Party"],
    #     "Winner Votes": winner_votes_int,
    #     "Runner Up": highest_votes_runner_up_candidate['Candidate Name'],
    #     "Runner Up Party": highest_votes_runner_up_candidate["Party"],
    #     "Runner Up Votes": first_runner_up_vote, 
    # }

    # runner_up_data.append(runner_up)

total_data = {
    "number_of_places_runner_up_less_than_1000": counter["1000"],
    "number_of_places_runner_up_less_than_2000_more_than_1000": counter["2000"],
    "number_of_places_runner_up_less_than_3000_more_than_2000": counter["3000"],
    "number_of_places_runner_up_less_than_4000_more_than_3000": counter["4000"],
    "number_of_places_runner_up_less_than_5000_more_than_4000": counter["5000"],
    "number_of_places_runner_up_less_than_6000_more_than_5000": counter["6000"],
    "number_of_places_runner_up_less_than_7000_more_than_6000": counter["7000"],
    "number_of_places_runner_up_less_than_8000_more_than_7000": counter["8000"],
    "number_of_places_runner_up_less_than_9000_more_than_80000": counter["9000"],
    "number_of_places_runner_up_less_than_10000_more_than_9000": counter["10000"],
    "number_of_places_runner_up_greater_than_10000": counter[">10000"],
    "number_of_places_runner_up_less_than_20000_more_than_10000": counter["20000"],
    "number_of_places_runner_up_less_than_30000_more_than_20000": counter["30000"],
    "number_of_places_runner_up_less_than_40000_more_than_30000": counter["40000"],    
    "number_of_places_runner_up_greate_than_40000": counter[">40000"],

    "No of constituency" : num_constituencies,
    "Constituency data": runner_up_strength_data
}

json_data = json.dumps(total_data, indent=2)

json_file_path = 'analysis_data/runner_up_lost_by_strength/runner_winner_by_strength_mizoram.json'

# Save the JSON data to a file
with open(json_file_path, 'w') as json_file:
    json_file.write(json_data)

print(f"JSON data saved to {json_file_path}")
