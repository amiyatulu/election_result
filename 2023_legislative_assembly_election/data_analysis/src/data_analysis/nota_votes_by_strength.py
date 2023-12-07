import pandas as pd

import json


json_file_path = "data/constituency_data_mizoram.json"
df = pd.read_json(json_file_path)

# print(df)

constituencies = df["Constituency"]
num_constituencies = df['Constituency'].nunique()

# print(constituencies.to_dict())

vote_wastage_data = []

number_of_places_nota_greater_than_1000 = 0
number_of_places_nota_greater_than_2000 = 0
number_of_places_nota_greater_than_3000 = 0



for constituency in constituencies:
    # print(constituency)
    candidate_infos = df[df["Constituency"] == constituency]["Candidates_info"]


    nota_frame = candidate_infos.apply(lambda x: [candidate for candidate in x if candidate['Candidate Name'] == 'NOTA'])


    nota = nota_frame.iloc[0]
    nota_votes_int = int(nota[0]["Votes"])
    if nota_votes_int > 1000:
        number_of_places_nota_greater_than_1000 = number_of_places_nota_greater_than_1000 + 1
    
    if nota_votes_int > 2000:
        number_of_places_nota_greater_than_2000 = number_of_places_nota_greater_than_2000 + 1

    if nota_votes_int > 3000:
        number_of_places_nota_greater_than_3000 = number_of_places_nota_greater_than_3000 + 1


    wastage = {
        "Constituency": constituency,
        "NOTA votes": nota_votes_int,
    }

    vote_wastage_data.append(wastage)

total_data = {
    "Nota votes greater than 1000" : number_of_places_nota_greater_than_1000,
    "Nota votes greater than 2000" : number_of_places_nota_greater_than_2000,
    "Nota votes greater than 3000" : number_of_places_nota_greater_than_3000,
    "No of constituency" : num_constituencies,
    "Constituency data": vote_wastage_data
}

json_data = json.dumps(total_data, indent=2)

json_file_path = 'nota_votes_mizoram.json'

# Save the JSON data to a file
with open(json_file_path, 'w') as json_file:
    json_file.write(json_data)

print(f"JSON data saved to {json_file_path}")
