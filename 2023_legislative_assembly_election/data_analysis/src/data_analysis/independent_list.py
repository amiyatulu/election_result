import pandas as pd
import json

json_file_path = "data/constituency_data_telangana.json"

df = pd.read_json(json_file_path)
constituencies = df["Constituency"]

lost_candidate_data = []

for constituency in constituencies:
    candidate_infos = df[df["Constituency"] == constituency]["Candidates_info"]    
    # print(candidate_infos.iloc[0])
    
    for candidate in candidate_infos.iloc[0]:
        if candidate['Status'] == 'lost' and (candidate['Party'] != "Bharatiya Janata Party" and candidate['Party'] != "Indian National Congress" and candidate['Party'] != "Bharat Rashtra Samithi"):
            candidate['Constituency'] = constituency
            lost_candidate_data.append(candidate)
    
    # print(lost_candidate_data)


sorted_candidates = sorted(lost_candidate_data, key=lambda x: int(x['Votes']), reverse=True)


json_data = json.dumps(sorted_candidates, indent=2)

json_file_path = 'analysis_data/independent_list/independent_list_telangana.json'

# Save the JSON data to a file
with open(json_file_path, 'w') as json_file:
    json_file.write(json_data)

print(f"JSON data saved to {json_file_path}")
